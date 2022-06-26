# **Git Bash** 사용
`~$`  
`sudo`  super user do (관리자 권한으로 실행)  
`ctrl + c` 명령 취소  

## Shell **command**
- `$`  Shell 을 입력할 수 있는 상태라는 의미  
- `$ ls`  List Segment  
- `$ ls -a`  숨김파일까지 보기  
- `$ cd`  Change Directory  
    　cd Documents/  
- `$ cd ..`  상위 폴더로 이동  
- `$ mkdir`  make directory, 새로운 디렉토리 생성  
- `$ pwd`  절대경로 `~` 의 의미 알 수 있다  
- `$ touch`  새로운 file 생성  
- `$ mv`  move 이동  
    　mv index.html coffee/  
    - `mv server.* coffee` :  * 서버라는 이름을 가진 모든 확장자명을 옮긴다  
    - `*.md`  md 확장자를 가지는 모든 파일  
- `$ mv` hello.py ./holla.py 이름 변경시에도 mv 사용  
- `$ ./`  현재 경로라는 뜻  
- `$ .filename`  파일 이름 앞에 `.` 붙으면 숨김파일  
- `$ clear`  화면 깨끗이 만듦  
- `$ cp`  copy 사본 만들기  
    　cp app.py coffee/             : 다른 위치에 사본 저장  
    　cp app.py ./app-copy.py  : 현재 위치에 다른 이름으로 사본 저장  
- `$ rm`  remove 파일 삭제  
    　rm app-copy.py  
- `$ rm -r`  or `$ rm -rf`  
    　rm -r coffee/  
    　rm -rf coffee/    f는 force 강제   
- `$ vi`  파일을 vim으로 열어라  
    　vi readme.md  
- `$ cat`  파일 내용을 확인할 때 사용. 처음 작성한 내용 확인  
    　cat readme.md  
- `$ python3` or `$ python`  파이썬 실행 결과 확인  
    　python hello.py  

## VIM  
: editor `vi`  
기본 normal mode  
To edit text, press `i` on normal mode  
To block text, press `v` on normal mode  
`shift` +`;` = `:` change to command mode  

### **Recap - Vim command**  
- `h` `j` `k` `l` - left, down, up, right  
- `i`  insert mode  
- `v`  visual mode  
- `ESC`  back to normal mode  
- `d`  delete  
- `dd`  delete a line / cut  
- `Y`  yank  
- `yy`  yank a line  
- `p`  paste  
- `u`  undo  
- `ctrl`+`r`  redo  
- `a`  append  
- `A`  append from end of line  
- `o`  open line(under)  
- `O`  open line(upper)  
- `H`  move to the top of the screen  
- `L`  move to the bottom of the screen  

### Command mode  
- `:q`  quit  
- `:q!`  quit discarding all changes  
- `:w`  write  
- `:wq`  write and quit  
- `:{number}`  jump to {number}th line.  

## VCS (Version Control System)  
= SCM (Source Code Management)  
< SCM (Software Configuration Management: 형상관리)  

---

# Git 실행 (add-commit-push)  

git 설치 확인(`$ git -v`)  

git 환경설정  

`$ git config --global user.name "당신의유저네임"`  

`$ git config --global user.email "당신의메일주소"`  

`$ git config --global core.editor "vim"`  

`$ git config --global core.pager "cat"`  

lg alias 설정: johanmeiring/gist:3002458  

`$ git config --list` 로 정상 설정 확인  

수정이 필요할 경우, `$ vi ~/.gitconfig` 에서 수정 가능  

---

> *Caution: **Do not git init** on any other directories*
> 
./dev 에서   

`$ git clone URL복사한것붙여넣기`  

`$ git status`  

`$ touch hello.py` → Untracked file 생김 (red color)  

`ls`  

`$ git add hello.py`  → Changes to be committed:  new file : ______ (green color)  

`$ git commit hello.py` → vim editor로 접속됨  

commit message 작성

제목과 내용사이에 빈칸 한줄 띄어 분리해줘야 함

제목만 봐도 알 수 있도록 잘 작성해야함

`$ git push origin main` 

`$ git remote` remote address를 보여줌

`$ git remote -v` remote 상세 address 보여줌

`$ git push origin main`

url을 일일이 적어주기 힘들기 때문에 ‘origin’ 으로 적어줌

`$ git lg` 작업한 log 확인 가능

⚠️ commit 할 때, `~~git commit -m~~` 가급적 쓰지 말기를 권고 

## Conventional Commits

[좋은 git 커밋 메시지를 작성하기 위한 7가지 약속 : NHN Cloud Meetup](https://meetup.toast.com/posts/106)

 ref: [https://www.conventionalcommits.org/ko/v1.0.0/](https://www.conventionalcommits.org/ko/v1.0.0/)

1. commit의 제목은 commit을 설명하는 하나의 구나 절로 완성
2. importanceofcapitalize Importance of Capitalize
3. **prefix 꼭 달기 -** *Commit Message 의 타입 (type)*
    - FEAT: 기능 개발 관련 (새로운 기능의 추가)
    - FIX: 오류 개선 혹은 버그 패치 (버그 수정)
    - DOCS: 문서화 작업 (문서 수정)
    - TEST: test 관련 (테스트 코트, 리펙토링 테스트 코드 추가)
    - CONF: 환경설정 관련
    - BUILD: 빌드 관련
    - CI: Continuous Integration 관련
    - STYLE: 스타일 관련 기능(코드 포맷팅, 세미콜론 누락, 코드 자체의 변경이 없는 경우)
    - REFACTOR: 코드 리펙토링
    - CHORE: 빌드 업무 수정, 패키지 매니저 수정(ex .gitignore 수정 같은 경우)

예시  
feat: Add server.py  
fix: Fix Typo server.py  
docs: Add README.md, LICENSE  
conf: Create .env, .gitignore, dockerfile  
BREAKING CHANGE: Drop Support /api/v1  
refactor: Refactor user classes  

## .gitignore  
.gitignore 는 git이 파일을 추적할 때, 어떤 파일이나 폴더 등을 추적하지 않도록 명시하기 위해 작성하며, 해당 문서에 작성된 리스트는 수정사항이 발생해도 git이 무시하게 됩니다.
특정 파일 확장자를 무시하거나 이름에 패턴이 존재하는 경우, 또는 특정 디렉토리 아래의 모든 파일을 무시할 수 있습니다.

## LICENSE  

가장 많이 사용하는 License  

- **MIT License**
MIT에서 만든 라이센스로, 모든 행동에 제약이 없으며, 저작권자는 소프트웨어와
관련한 책임에서 자유롭습니다.
- **Apache License 2.0**
Apache 재단이 만든 라이센스로, 특허권 관련 내용이 포함되어 있습니다.
- **GNU General Public License v3.0**
가장 많이 알려져있으며, 의무사항(해당 라이센스가 적용된 소스코드 사용시 GPL 을 따라야 함)

**Deal with .ipynb**
[https://www.reviewnb.com/](https://www.reviewnb.com/)

.ipynb(jupyter notebook)은 json 기반이기 때문에 source control이 쉽지 않음 → extension 으로 극복

또는 [https://github.com/jupyter/nbconvert](https://github.com/jupyter/nbconvert) 으로 .py or .html 로 변환

---

# Branch

분기점을 생성하여 독립적으로 코드를 변경할 수 있도록 도와주는 모델

`$ git branch`  Show available local branch

`$ git branch -r`  Show available remote branch

`$ git branch -a`  Show available All branch

`$ git branch stem`  Create branch (branch name : stem)

`$ git checkout stem`  Checkout branch = `$ git switch stem`

`$ git checkout -b new-stem`  Create & Checkout branch

`$ git commit -a -m 'edit readme.md'`  make changes inside readme.md

**`$ git switch main`**

`$ git merge stem`  merge branch

`$ git branch -D stem`  delete branch

`$ git push origin stem`  push with specified remote branch

`$ git diff master stem`  see the difference between two branches

새로 만든 branch에서 첫 push 할 때는 꼭 `-u` upstream 표시 해줘야함

`**$ git push -u origin** stem`

---

1. git bash에서 .dev/ 에 팀 깃허브 클론을 만들고 (`$ git clone {팀 깃허브 주소}`)
2. 클론되서 생성된 'study' directory로 들어감 (`cd study`)
3. 제가 사용할 새로운 branch 생성 (`$ git branch {브랜치명}`)
4. `$ git switch {브랜치명}`
5. `$ git push -u origin {브랜치명}`

---

# Revert

`$ git mv 기존파일명  변경할파일명`  파일 이름 변경됨 (renamed)

그냥 `$ mv 기존파일명  변경할파일명` 이렇게 하면 기존 파일은 삭제되고 새 파일 형성된 것으로 인식

⇒ 파일의 history를 남기기 위해서는 삭제 후 생성이 아닌 이름바꾸기로 추적

`$ git checkout -- .` or `$ git checkout -- {filename}`  Undoing

`$ git rm -f {filename}`   Unstaging and Remove

`$ git commit --amend`  Edit latest commit

`$ git rebase -i <commit>`  Edit prior commit

`$ git rebase --abort`  abort rebase

`$ git rebase --continue`  Complete rebase

`$ git reset HEAD {filename}`   Unstaging

⚠️ 협업 시, reset은 **worst case** 이다.  

(ex. 직전 3개의 commit을 삭제한 후, remote에 강제 push)  
다른 cloned repo에 존재하던 commit log로 인해 파일이 살아나거나, 과거 이력이 깔끔히 사라져 commit log tracking이 힘들어짐.  
⇒ solution: 잘못한 이력도 commit으로 박제하고 수정한 이력을 남기자!  

👍 **Best case: Revert**  

(ex. 현재 HEAD에서 직전의 3개의 commit을 순서대로 거슬러 올라가 해당 내역에 대해 commit, push 수행)

```bash
$ git revert --no-commit HEAD~3..
$ git commit
$ git push origin {branch}
```

잘못하기 전 과거로 돌아가 최신을 유지하면서 되돌렸다는 이력을 commit으로 남겨 모든 팀원이 이 사항을 공유하고 주지시킬 수 있음.

- commit을 따로 안할땐 `--no-edit`
- merge commit을 되돌릴 땐 `-m ( $git revert -m {1 or 2} {merge commit id} )`

---

# Issue & Projects  

- Issue : 프로젝트, 레포와 관계된 모든 해야할 일과 버그, 개선사항 등을 기록  
- Projects : 해야할 일의 진도에 따른 구성과 우선순위 지정  


# Trailing comma  
```‘tulip’ ,``` 
이렇게 마지막 문장에 콤마를 미리 붙여넣으면, 추후에 내용 추가했을 때 아랫줄에 추가된 줄만 git에서 업데이트 된것으로 뜨기 때문에 이런식으로 작성하는 것이 좋다.  
