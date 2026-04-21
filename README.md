# lorg

URL을 단축하고 Org-mode 링크 형식으로 출력하는 CLI 도구입니다.

## 개발 실행

```bash
uv run python lorg https://example.com
uv run python lorg https://example.com "Custom Title"
```

## 모듈 실행

```bash
uv run python -m lorg https://example.com
```

## 설치 실행 (pip --user)

```bash
PYTHONUSERBASE="$HOME/.local" python -m pip install --user .
```

macOS/Homebrew Python에서 PEP 668 오류가 나면 아래처럼 설치합니다.

```bash
PYTHONUSERBASE="$HOME/.local" python -m pip install --user --break-system-packages .
```

설치 후 바이너리는 보통 `$HOME/.local/bin/lorg`에 생성됩니다.

`$HOME/.local/bin`이 PATH에 있으면 다음처럼 바로 실행할 수 있습니다.

```bash
lorg https://example.com
```
