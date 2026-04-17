default:
    @just --list

install:
    uv sync --group dev

dev:
    uv run ptw .

test:
    uv run pytest --cov=src tests/

check:
    uv run ruff check src
    uv run ty check src

format:
    uv run ruff format src

docs-serve:
    uv run zensical serve

docs-build:
    uv run zensical build

docs-deploy:
    echo "deploying docs"
    # uv run zensical deploy

publish:
    echo "publish package"
