# Goldstonian Concordance Bible Canon Game Engine

This repository contains the data and engine used to generate trivia questions and educational gameplay content from the full 81-book biblical canon used by the Goldstonian Concordance Bible (GCB).

The system automatically generates thousands of questions using structured scripture datasets and templated question models.

The generated content powers:

- Board games
- Mobile apps
- Web trivia
- YouTube learning content
- SydTek Scholars coursework

## Architecture

Bible Text → Structured Canon Dataset → Trivia Generator → Game Outputs

## Key Features

• Automatic trivia generation  
• Mirror–Water–Fire theological questions  
• Board game card export  
• YouTube trivia automation  
• Mobile trivia API dataset

## Dataset Size

Expected outputs:

- 35,000+ verses indexed
- 100,000+ generated trivia questions
- 81-book canon coverage

## Repository Sections

data/
Structured biblical datasets

templates/
Question generation templates

engine/
Core generation engine

exports/
Generated trivia outputs

boardgame/
Board layout and mechanics

scripts/
Automation tools

## Usage

Generate all questions:

```bash
python scripts/generate_all_questions.py