#!/usr/bin/env python3
"""A lightweight creative writing assistant for novels, scripts, lyrics, scenes, and dialogues."""

from __future__ import annotations

from dataclasses import dataclass
from textwrap import dedent


@dataclass
class ProjectContext:
    writing_type: str
    genre: str
    mood: str
    theme: str
    setting: str
    sensory_details: str
    key_characters: str
    conflict: str
    goal: str
    voice_style: str


def ask(prompt: str) -> str:
    value = input(f"{prompt}: ").strip()
    return value or "Not specified"


def build_plan(context: ProjectContext) -> str:
    return dedent(
        f"""
        1) Foundation
           - Writing type: {context.writing_type}
           - Genre and mood: {context.genre} / {context.mood}
           - Core theme: {context.theme}

        2) Character + Environment Alignment
           - Primary setting: {context.setting}
           - Human texture via sensory anchors: {context.sensory_details}
           - Character focus: {context.key_characters}

        3) Dramatic Drive
           - Conflict pressure: {context.conflict}
           - Immediate objective of this piece: {context.goal}

        4) Drafting Blueprint
           - Voice style: {context.voice_style}
           - Draft in short beats (setup -> tension -> turn -> residue)
           - Keep language grounded, emotional, and imperfect where natural.

        5) Revision Loop
           - Pass 1: Sharpen imagery tied to location and body language.
           - Pass 2: Reduce generic lines; add character-specific words.
           - Pass 3: Keep rhythm and silence (pauses, subtext, unfinished thoughts).
        """
    ).strip()


def build_prompt(context: ProjectContext) -> str:
    return dedent(
        f"""
        You are a collaborative writing partner.

        TASK
        Create a {context.writing_type} draft with a raw, human tone.

        CREATIVE DIRECTION
        - Genre: {context.genre}
        - Mood: {context.mood}
        - Theme: {context.theme}
        - Voice style: {context.voice_style}

        WORLD + ATMOSPHERE
        - Setting: {context.setting}
        - Sensory texture: {context.sensory_details}

        CHARACTER FOCUS
        - Main characters: {context.key_characters}
        - Core conflict: {context.conflict}
        - Goal for this draft: {context.goal}

        WRITING CONSTRAINTS
        - Keep dialogue natural; avoid polished corporate language.
        - Include environmental interaction (weather, sounds, objects, space pressure).
        - Show emotional subtext through gestures, pauses, and contradictions.
        - End with a lingering emotional beat rather than a neat conclusion.

        OUTPUT FORMAT
        1) Title options (3)
        2) Draft
        3) Notes on why the draft feels human (bullet list)
        4) Optional alternate ending (short)
        """
    ).strip()


def build_follow_up_prompts(context: ProjectContext) -> list[str]:
    return [
        f"Rewrite the {context.writing_type} with higher tension and less exposition.",
        "Keep the same plot but make each line of dialogue reveal hidden motive.",
        f"Shift the mood from {context.mood} to bittersweet while preserving continuity.",
        "Add stronger environmental cues every 2-3 paragraphs without over-describing.",
        "Give me two alternate versions: one intimate and one cinematic.",
    ]


def run() -> None:
    print("\n=== Creative Writing Assistant Builder ===")
    print("This tool creates a tailored writing plan + master prompt for your project.\n")

    context = ProjectContext(
        writing_type=ask("What are you writing? (novel/script/lyrics/scene/dialogue)"),
        genre=ask("Genre"),
        mood=ask("Mood/tone"),
        theme=ask("Theme/message"),
        setting=ask("Setting/environment"),
        sensory_details=ask("Sensory details to emphasize (sound/smell/weather/textures)"),
        key_characters=ask("Key characters and relationship dynamics"),
        conflict=ask("Main conflict"),
        goal=ask("What should this specific piece accomplish?"),
        voice_style=ask("Voice style (simple poetic gritty etc.)"),
    )

    print("\n--- YOUR WRITING PLAN ---")
    print(build_plan(context))

    print("\n--- MASTER PROMPT (copy into your AI writing tool) ---")
    print(build_prompt(context))

    print("\n--- FOLLOW-UP PROMPTS FOR ITERATION ---")
    for i, prompt in enumerate(build_follow_up_prompts(context), start=1):
        print(f"{i}. {prompt}")

    print("\nTip: Start with one emotional moment, then expand scene by scene.")


if __name__ == "__main__":
    run()
