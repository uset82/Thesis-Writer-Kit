#!/usr/bin/env python3
"""
ABOUTME: OpenAI-compatible adapter for OpenDraft's Gemini-style interface
ABOUTME: Provides generate_content and Gemini-like response objects
"""

from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class _OpenAIPart:
    """Minimal Gemini-style content part with text."""
    text: str


@dataclass
class _OpenAIContent:
    """Container for content parts."""
    parts: List[_OpenAIPart]


@dataclass
class _OpenAICandidate:
    """Gemini-style candidate wrapper."""
    content: _OpenAIContent
    finish_reason: int = 1  # 1 = STOP (Gemini-style)


class OpenAIResponse:
    """Gemini-style response wrapper for OpenAI outputs."""

    def __init__(self, text: str):
        self._text = text or ""
        self.candidates = [_OpenAICandidate(content=_OpenAIContent(parts=[_OpenAIPart(self._text)]))]

    @property
    def text(self) -> str:
        if not self._text:
            raise ValueError("No text content in response")
        return self._text


class OpenAIChatAdapter:
    """
    Adapter that exposes a Gemini-like interface for OpenAI-compatible clients.

    This enables OpenDraft to run without changing the rest of the pipeline.
    """

    def __init__(self, client: Any, model: str, temperature: float = 0.7):
        self._client = client
        self._model = model
        self._temperature = temperature

    def generate_content(self, prompt: str, generation_config: Optional[Any] = None) -> OpenAIResponse:
        """Generate content using OpenAI-compatible chat completions."""
        _ = generation_config  # Unused, kept for Gemini-compatibility

        response = self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self._temperature,
        )
        text = response.choices[0].message.content if response.choices else ""
        return OpenAIResponse(text or "")
