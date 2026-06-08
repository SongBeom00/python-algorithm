# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python 기초 학습용 저장소로, Jupyter Notebook(`.ipynb`) 파일들로 구성된 단계별 실습 자료입니다.
패키지 관리는 `uv`를 사용합니다.

## Commands

```bash
# 의존성 설치
uv sync

# 메인 스크립트 실행
uv run python main.py

# 코드 포맷팅
uv run black .

# 코드 품질 검사
uv run pylint main.py

# Jupyter Notebook 실행
uv run jupyter notebook
```

## Architecture

- **`*.ipynb`** : 번호 순서대로 이어지는 Python 기초 실습 노트북 (1~9번)
- **`main.py`** : 프로젝트 진입점 (현재 placeholder)
- **`pyproject.toml`** : uv 기반 프로젝트 설정, Python >= 3.11 필요
- **`Python Basic 정리.md`** : 1~8번 노트북 내용 마크다운 요약본
