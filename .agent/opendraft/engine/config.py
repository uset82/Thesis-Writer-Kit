#!/usr/bin/env python3
"""
ABOUTME: Centralized configuration management for OpenDraft
ABOUTME: Single source of truth for all settings, models, and environment variables
"""

import os
from dataclasses import dataclass, field
from typing import Literal, Optional, cast
from pathlib import Path


# Try to load environment variables from .env files
# Priority: .env.local > .env (local overrides default)
try:
    from dotenv import load_dotenv

    # Get directory where config.py is located
    config_dir = Path(__file__).parent
    project_root = config_dir.parent

    # Load .env first (defaults)
    env_candidates = [
        (project_root / '.env', False),
        (config_dir / '.env', False),
        (project_root / '.env.local', True),
        (config_dir / '.env.local', True),
    ]

    for env_path, override in env_candidates:
        if env_path.exists():
            load_dotenv(env_path, override=override)

except ImportError:
    # dotenv is optional - will use system environment variables
    pass


@dataclass
class ModelConfig:
    """
    Model configuration with sensible defaults.

    Supports Gemini models with configurable parameters.
    """
    provider: Literal['gemini', 'claude', 'openai'] = field(
        default_factory=lambda: cast(Literal['gemini', 'claude', 'openai'], os.getenv('MODEL_PROVIDER', 'gemini').lower())
    )
    model_name: str = field(default_factory=lambda: os.getenv('GEMINI_MODEL', 'gemini-3-pro-preview'))
    temperature: float = 0.7
    max_output_tokens: Optional[int] = None

    def __post_init__(self):
        """Validate model configuration."""
        valid_providers = ('gemini', 'claude', 'openai')
        if self.provider not in valid_providers:
            raise ValueError(
                f"Invalid provider: {self.provider}. Valid options: {', '.join(valid_providers)}"
            )

        if self.provider == 'openai':
            self.model_name = os.getenv('OPENAI_MODEL', os.getenv('MODEL_NAME', 'gpt-4o-mini'))
            return

        if self.provider == 'claude':
            self.model_name = os.getenv('CLAUDE_MODEL', os.getenv('MODEL_NAME', 'claude-3-5-sonnet-20241022'))
            return

        valid_models = [
            'gemini-3-pro-preview',  # Default - highest quality
            'gemini-3-flash',        # Fast, cost-effective
            'gemini-2.5-pro',
            'gemini-2.5-flash',
            'gemini-2.0-flash',
            'gemini-2.0-pro-exp-02-05',
            'gemini-1.5-pro',
            'gemini-1.5-flash',
        ]
        self.model_name = os.getenv('GEMINI_MODEL', self.model_name)
        if self.model_name not in valid_models:
            # If user supplies custom valid model name, allow it with a warning
            pass


@dataclass
class ValidationConfig:
    """Configuration for validation agents (Skeptic, Verifier, Referee)."""
    use_pro_model: bool = field(default_factory=lambda: os.getenv('USE_PRO_FOR_VALIDATION', 'false').lower() == 'true')
    pro_model_name: str = field(default_factory=lambda: os.getenv('VALIDATION_MODEL', 'gemini-2.5-pro'))
    validate_per_section: bool = True  # Always validate each section independently

    def get_validation_model(self, base_model: str) -> str:
        """Return appropriate model for validation tasks."""
        return self.pro_model_name if self.use_pro_model else base_model


@dataclass
class PathConfig:
    """Path configuration for outputs and prompts."""
    project_root: Path = field(default_factory=lambda: Path(__file__).parent)
    output_dir: Path = field(default_factory=lambda: Path('tests/outputs'))
    prompts_dir: Path = field(default_factory=lambda: Path('prompts'))

    def __post_init__(self):
        """Ensure paths are absolute."""
        self.output_dir = self.project_root / self.output_dir
        self.prompts_dir = self.project_root / self.prompts_dir


@dataclass
class AppConfig:
    """
    Application-wide configuration.

    Single source of truth for all settings across the application.
    Follows SOLID principles and provides type-safe access to configuration.
    """
    # API Keys
    google_api_key: str = field(default_factory=lambda: os.getenv('GOOGLE_API_KEY', ''))
    anthropic_api_key: str = field(default_factory=lambda: os.getenv('ANTHROPIC_API_KEY', ''))
    openai_api_key: str = field(default_factory=lambda: os.getenv('OPENAI_API_KEY', ''))
    openai_base_url: str = field(default_factory=lambda: os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1'))

    # Sub-configurations
    model: ModelConfig = field(default_factory=ModelConfig)
    validation: ValidationConfig = field(default_factory=ValidationConfig)
    paths: PathConfig = field(default_factory=PathConfig)

    # Citation and paper settings
    citation_style: str = field(default_factory=lambda: os.getenv('CITATION_STYLE', 'apa'))
    ai_detection_threshold: float = field(default_factory=lambda: float(os.getenv('AI_DETECTION_THRESHOLD', '0.20')))

    def __post_init__(self):
        """Validate configuration on initialization."""
        pass

    def validate_api_keys(self) -> None:
        """
        Validate that required API keys are present.

        Call this before operations that need API access.
        Raises ValueError if required keys are missing.
        """
        if self.model.provider == 'gemini' and not self.google_api_key:
            raise ValueError(
                "GOOGLE_API_KEY environment variable is required for Gemini models. "
                "Set it in .env file or environment. "
                "Get your key at: https://makersuite.google.com/app/apikey"
            )

        if self.model.provider == 'claude' and not self.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY required for Claude models")

        if self.model.provider == 'openai' and not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY required for OpenAI models")

    @property
    def has_api_key(self) -> bool:
        """Check if required API key is configured (without raising)."""
        if self.model.provider == 'gemini':
            return bool(self.google_api_key)
        if self.model.provider == 'claude':
            return bool(self.anthropic_api_key)
        if self.model.provider == 'openai':
            return bool(self.openai_api_key)
        return False


# Global configuration instance - lazy loaded
_config: Optional[AppConfig] = None


def get_config() -> AppConfig:
    """
    Get the global configuration instance (lazy loaded).

    Returns:
        AppConfig: The application configuration
    """
    global _config
    if _config is None:
        _config = AppConfig()
    return _config


def update_model(model_name: str) -> None:
    """
    Update the model name at runtime.

    Args:
        model_name: New model name to use
    """
    cfg = get_config()
    cfg.model.model_name = model_name
    cfg.model.__post_init__()  # Re-validate


if __name__ == '__main__':
    # Configuration validation test
    cfg = get_config()
    print("[OK] Configuration loaded successfully")
    print(f"Model: {cfg.model.model_name}")
    print(f"Provider: {cfg.model.provider}")
    print(f"API Key configured: {cfg.has_api_key}")
    print(f"Validation per section: {cfg.validation.validate_per_section}")
    print(f"Output directory: {cfg.paths.output_dir}")
