# lorg

URL을 단축하고 Org-mode 링크 형식으로 출력하는 CLI 도구입니다.

## 개발 실행

```bash
uv run python lorg https://example.com
# output: [[https://example.com][Custom Title]]
uv run python lorg https://example.com "Custom Title"
```

## 모듈 실행

```bash
uv run python -m lorg https://example.com
```

## 설치 실행

권장 방법은 `uv tool` 또는 `pipx`입니다.

### 1) uv tool (권장)

```bash
uv tool install --from . lorg --force
```

### 2) pipx

```bash
pipx install .
```

### 3) pip --user (fallback)

```bash
PYTHONUSERBASE="$HOME/.local" python -m pip install --user --break-system-packages .
```

`uv run ... pip install --user`는 가상환경에서 실행되므로 `--user` 설치가 불가능합니다.
Homebrew Python 환경에서는 PEP 668 정책 때문에 `--break-system-packages`가 필요할 수 있습니다.

설치 후 바이너리는 보통 `$HOME/.local/bin/lorg`에 생성됩니다.

`$HOME/.local/bin`이 PATH에 있으면 다음처럼 바로 실행할 수 있습니다.

```bash
lorg https://example.com
```
