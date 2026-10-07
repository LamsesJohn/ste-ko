## 핵심 차이

둘 다 한 브랜치의 변경 사항을 다른 브랜치에 통합하는 명령이지만, **히스토리를 다루는 방식**이 다릅니다.

### git merge
두 브랜치의 끝을 합치는 **머지 커밋**을 새로 만듭니다. 기존 커밋은 그대로 보존됩니다.

```
      A---B---C  feature
     /         \
D---E---F---G---M  main   (M = 머지 커밋)
```

```bash
git checkout main
git merge feature
```

### git rebase
feature 브랜치의 커밋들을 **main의 최신 커밋 위에 다시 적용**합니다. 커밋이 새로 만들어지므로 해시가 바뀌고, 히스토리가 일직선이 됩니다.

```
              A'--B'--C'  feature
             /
D---E---F---G  main
```

```bash
git checkout feature
git rebase main
```

## 비교

| | merge | rebase |
|---|---|---|
| 히스토리 | 분기/합류가 그대로 남음 | 일직선으로 깔끔함 |
| 커밋 | 기존 커밋 보존 + 머지 커밋 추가 | 커밋을 새로 작성 (해시 변경) |
| 안전성 | 히스토리를 변경하지 않아 안전 | 히스토리를 다시 쓰므로 주의 필요 |
| 충돌 해결 | 한 번에 해결 | 커밋마다 해결해야 할 수 있음 |
| 추적 | 언제 합쳐졌는지 명확 | 합류 시점 정보가 사라짐 |

## 사용 가이드

- **이미 push해서 다른 사람이 쓰는 브랜치는 rebase하지 마세요.** 해시가 바뀌어 협업자의 히스토리와 충돌합니다. (`git push --force`가 필요해지는 상황)
- **내 로컬 feature 브랜치를 최신 main에 맞추고 싶을 때**는 rebase가 깔끔합니다.
- **main 같은 공용 브랜치에 통합할 때**는 merge(또는 PR의 squash/merge)가 일반적입니다.
- 흔한 워크플로: feature에서 `git rebase main`으로 최신화 → main에서 `git merge feature` (fast-forward 가능).

원하시면 충돌 해결 방법이나 `rebase -i`(커밋 정리)도 설명드릴게요.
