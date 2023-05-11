# 🐶 네모난친구들
![thumb-removebg](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/838d2084-f492-463a-8a83-bd7e67ab7198)


#### 🟩 UCC : [링크](https://www.youtube.com/watch?v=gl21A0Yb4P4)

#### 🟩 시연 시나리오 : [링크](https://file.notion.so/f/s/2832d075-6af8-439e-ae21-928dc3aadfee/%ED%8A%B9%ED%99%94-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%9C%EC%97%B0-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4.pdf?id=9783cf2a-c7ad-4a76-a9e3-42641536bcc9&table=block&spaceId=fd3ef439-43cf-4af5-94b3-dfaf012b4bf5&expirationTimestamp=1683880063085&signature=tjYLXZuHOB3NOGKVGrHpoJ8pOr-am4IfYXCkSxmFt14&downloadName=%EB%84%A4%EB%AA%A8%EB%82%9C+%EC%B9%9C%EA%B5%AC%EB%93%A4+%EC%82%AC%EC%9A%A9+%EA%B0%80%EC%9D%B4%EB%93%9C.pdf)
      
      
---
## ✨Overview
1. 인공지능 기술을 접목한 동물 키우기 게임입니다. 주어진 필드를 자유롭게 꾸미고 나만의 동물과 상호작용 해보세요!

## 🧑‍🤝‍🧑 팀 소개    
![팀원소개](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/8cf0ca3e-f3e6-4c07-b645-e446cbbe4c1f) 

## ⭐ 핵심 서비스

### º 먹이주기
```
동물이 좋아하는 먹이를 직접 그리면, 인공지능이 무슨 그림인지 판단한다.    
판단된 결과들 중 하나를 누르면 동물이 먹을 수 있는지 확인하여, 
해당 동물이 먹을 수 있는 음식이 맞다면(동물에게 맞는 음식은 도감에서 확인 가능) 음식을 줄 수 있다.     
음식을 먹으면 동물의 애정도가 올라가며, 이는 4시간에 한 번씩 줄 수 있다.     
```
![13 동물먹이주기_바나나](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/da2db94f-36ba-424c-815f-af37d71ba657)

### º 대화하기
```
하단 중앙에 있는 말풍선 버튼을 누르면 동물에게 말을 걸 수 있다.     
지어준 동물 별명과 함께 명령어를 말하면 인공지능이 음성을 인식한다.     
이렇게 해당 동물의 단계에서 할 수 있는 명령어라면 행동을 보여주고, 존재하지 않는 명령어를 말하면 실패했다는 메세지를 보여준다.     
대화하기의 경우 횟수 제한은 없지만, 경험치와 골드 보상은 한 동물 당 하루에 5번만 지급된다.    
```
![9 음성명령](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/2e9d2136-55f7-4ae6-bc01-4551a4956bf9)

### º 놀아주기 - 끝말잇기
```
마이크 버튼을 누르고 3초 안에 단어를 말하면, 인공지능이 음성을 인식한다.    
끝 음절과 이어지지 않는 단어를 말하거나, 사전에 없는 단어라면 게임이 끝난다.     
이렇게 끝말잇기는 성공한 횟수에 따라 경험치를 얻을 수 있고, 사용자가 이길 경우 보상은 2배가 된다.        
(단, 한 동물 당 하루에 5번까지만 할 수 있습니다)
```
![14 끝말잇기](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/48b6003e-7720-4f22-a5d1-2c3a06ed38c2)

### º 놀아주기 - 미로찾기
```
제한된 시간 동안 동물을 움직여 미로에 존재하는 동전을 최대한 많이 먹어야한다.   
동전을 먹으면 이렇게 제한 시간이 증가하며, 동물의 성장 단계에 따라, 골드와 제한 시간이 상이하다.   
동전을 다 먹거나, 시간이 끝나거나, 나가기 버튼을 누르면 먹은 동전만큼 골드를 받는다.    
미로의 경우 매번 새롭게 랜덤으로 생성된다.    
```
![15  (1)미로찾기_깃허브리드미용량조절](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/dfd0ba1d-1dc4-4063-b316-aeb897af25ec)

### º 상점 / 보관함
```
상점에 들어가면 조경을 구매할 수 있다.     
구매한 조경은 보관함에 저장되며, 보관함에서 조경을 누르면 배치모드로 변경됩니다.     
```
![5 상점,보관함](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/11afec8a-9cca-4238-be7e-ca6b1b3ae0a6)

### º 필드 꾸미기
```
배치모드(필드 꾸미기)에서는 선택한 조경(from 보관함)을 다른 조경과 겹치지 않는 초록색 칸에 배치할 수 있고, 각도도 변경 가능하다.     
기존에 배치한 조경을 다시 배치하려면, 조경을 2-3초 꾹 눌러 바로 배치모드로 변경할 수 있다.
```
![7 배치모드](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/d953d29e-8422-40d8-8d25-903be16cc806)

## 뽑기
```
상점에서 판매하는 조경 및 뽑기로만 얻을 수 있는 희귀 조경, 성장의 물약, 새로운 동물 친구 등을 뽑을 수 있다.   
```
![11  (1) 뽑기_깃허브리드미용량조절](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/d20308a9-644b-4cba-b350-2610a5a750f6)

## ✨ 주요 기능
---
- 서비스 설명 : 이미지 분류를 통한 먹이주기, 음성 텍스트 변환(STT)을 이용한 대화하기 등의 기능을 통해 내 동물을 키우고, 그 과정에서 받게 되는 골드를 통해 새 동물이나 조경을 얻어 필드를 꾸밀 수 있습니다.
- 주요 기능 :
    - QuickDraw 데이터셋 을 이용한 낙서 이미지 분류 기능을 통해 동물에게 먹이를 직접 그려서 줄 수 있는 기능
    - STT 모델을 이용한 동물과 대화하기, 끝말잇기 기능
    - 조경을 상점에서 구매하고, 필드에 배치할 수 있는 기능
    - 미로를 돌아다니며 골드를 모을 수 있는 미로찾기 게임

### 개발 환경

---

**Backend**
- Visual Studio Code
- pyton 3.10.5
- Django 3.2.12
- simple jwt
- AWS EC2
- MySQL 8.0.30
- redis

**Application**
- Visual Studio Code
- Unity 2020.3.38.f1
- Baracuda 1.0.4

**AI**
- Jupyter notebook(GPU Server)
- tensorflow-gpu 2.1.0
- Keras 2.10.0
- kospeech
- pytorch 1.12.1
- QuickDraw
- AI HUB 한국어 음성 데이터셋
- VITO
- Googlespeech

**CI/CD**
- AWS EC2 ubuntu 20.04
- docker 20.10.18
- nginx 1.18.0
- jenkins 2.361.1

#### 각 개발 환경 별 포팅 매뉴얼

Back-end : [링크](https://file.notion.so/f/s/60a8a820-ba6a-4297-b903-de240046c817/Backend.md?id=2f2e91cc-05b3-4778-9a9d-0687ba506a60&table=block&spaceId=fd3ef439-43cf-4af5-94b3-dfaf012b4bf5&expirationTimestamp=1683882484163&signature=iJx8CZrGnPfncZwFUk1P8gbr_JaxhhHja1JoVtrg740&downloadName=Backend.md)

Unity (Front-end) : [링크](https://file.notion.so/f/s/5e7977f0-1fd8-4a64-bb9b-a1e9fcfff048/%EC%9C%A0%EB%8B%88%ED%8B%B0%EB%B9%8C%EB%93%9C%ED%85%8C%EC%8A%A4%ED%8A%B8.pdf?id=16661283-5ba7-48bc-a3d9-79298d1ed6cd&table=block&spaceId=fd3ef439-43cf-4af5-94b3-dfaf012b4bf5&expirationTimestamp=1683882513731&signature=9HE5QlyWlLRXGPKDGU1gjMtb13WnjXQfx_kbgfbKpfY&downloadName=%EC%9C%A0%EB%8B%88%ED%8B%B0%EB%B9%8C%EB%93%9C%ED%85%8C%EC%8A%A4%ED%8A%B8.pdf)

### 아키텍쳐 구성도

---
![아키텍처](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/d3777529-7391-46d7-a8e9-c3fdaaa007e8)

### Jenkins를 이용한 CD 구축 및 SSL 인증서 적용

---

백엔드 CICD 배포 및 SSL 인증서 적용 과정은 [여기](https://lab.ssafy.com/s07-webmobile3-sub2/S07P12C102/-/blob/master/CICD.md)에서 설명해두었습니다.

### 특이점

---

- Unity
동물 키우기를 기획하는 도중 아이소매트릭 형태의 디자인 아이디어가 나왔고, 동물에 대해 생동감을 부여해주고 필드를 꾸밀 수 있도록 하기 위해서 3D 화면으로 구현하기로 결정했습니다. three.js, Unity, AndroidStudio 등의 후보를 두고 고민하고 토의를 한 결과 Unity를 사용하는 것으로 결정했습니다.

- Baracuda
Unity에서 AI모델을 사용하기 위해서는 해당 라이브러리를 꼭 사용해야 했습니다. 기존의 Keras나 Pytorch로 학습시킨 모델을 ONNX 파일로 변환하여 Baracuda 라이브러리가 인식할 수 있도록 했고, Baracuda를 이용하여 그림을 인식하는 AI를 구현하였습니다.

- Redis
저희 프로젝트의 기능 중, 끝말잇기의 경우 App과 Backend가 지속적으로 통신하면서 데이터 교환이 이루어집니다. 이 때, 한 게임 씩 단발성으로 진행되는 형태의 게임인 끝말잇기에 관계형 DB를 그대로 사용하는 것은 효율이 떨어지고 속도가 느릴 것이라고 생각했습니다. 중복사용 단어의 처리와 통신속도 향상을 위해서 Redis를 사용하였습니다.

- QuickDraw Model
저희는 AI 음성 팀이지만, 프로젝트 기획 내용에 이미지 처리까지 포함이 되어있었기 때문에 이미지 처리 모델도 학습시켜 만들었습니다. 모든 학습은 SSAFY에서 제공한 GPU 서버에서 진행하였습니다. QuickDraw 데이터셋을 이용한 낙서 인식 모델은 Keras를 이용해 학습시켰습니다. 46만개의 이미지를 5 Epoch만큼 돌렸습니다. GPU서버에서 병렬 처리를 할 수 있도록 설정하여 이미지 학습시간을 21초까지 단축시켰습니다.

- 한국어 음성인식 모델
AI HUB에서 내려받은 한국어 데이터셋을 이용한 STT(Speech to Text) 모델은 Pytorch와 Kospeech를 이용하여 학습시켰습니다. 음성 데이터 양이 1000시간으로, 20 Epoch만큼 돌려 총 학습시간은 220시간이 걸렸습니다. 해당 모델에, Vito 및 GoogleSpeech API를 함께 사용하여 인식이 잘 되는 데이터를 반환하도록 설정했습니다.

- 배포
Docker, Nginx, Jenkins를 이용하여 무중단 자동 배포를 구축하였습니다. Nginx는 Aws에 서버를 띄워 FE를 서비스했고, Django 서버는 도커의 컨테이너로 넣어 AWS EC2의 Nginx에 리버스 프록시로 연결했습니다.



### 협업

---
- Git
- Jira
- Notion
- Mattermost
- Webex
- discode


### ✨ Plastic SCM Commit Rule (Unity 협업 툴)

---

## 📌 브랜치 생성 관련

- 최상단 브랜치 - main
- main/test → scm 브랜치 테스트 브랜치이므로 신경쓰지 않아도 된다
- main 아래에 기능별로 브랜치를 생성하고, 큰 기능이 같은 경우 _(언더바로 묶는다)
    - 예시) 로그인의 경우
        - main/login, main/login_certified

## 📌 Commit Rule

- [본인이름] 기능상세설명
- 디폴트로 변경되는 값만 커밋할 경우(본인의 변경사항이 없는데 변경사항이 갑자기 생긴경우)
    
    본인 이름만 써서 커밋하기 (EX. [본인이름])
    

## 📌 병합 (Merge)

- 1)워크스페이스 업데이트 후 !
- 2) 하위브랜치에서 일단 변경사항을 커밋하기
- **병합하려는 상위브랜치로 워크스페이스를 바꿔준 후**
- 병합하려는 하위 브랜치를 우클릭하여 **“이 브랜치에서 병합”** 선택
- 마지막으로, 변경된 내용을 가져왔으므로 상위브랜치에서 재커밋을 해줘야 함

###  ER Diagram

---

![ERD](https://github.com/eodhlwjr97/2023-1-Algorithm/assets/99021614/54e06f63-1283-489e-8ac7-e31db3f570cf)

