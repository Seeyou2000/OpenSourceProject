# CookIndoor
<p align="center">
<img src="CookIndoor/demo_image/start2.png" alt="start image" width="80%" height="60%">
</p>
CookIndoor는 openCV를 이용한 요리 시뮬레이션 게임입니다.

## Contents
* ### [Feature](#feature-1)
* ### [How to start?](#how-to-start-1)
* ### [How to play?](#how-to-play-1)
* ### [Demo video](#demo-video-1)

## Feature
<p align="center">
<img src="CookIndoor/demo_image/maindish.png" alt="maindish image" width="80%" height="60%">
</p>


## How to start?
### 환경 설정
먼저 캠을 사용할 수 있는 장치가 필요합니다.

#### pip install
```
pip install opencv
or
pip install opencv-python
```

```
pip install mediapipe
```
```
pip install numpy
```
```
pip install pygame
```

### 어플리케이션 시작
필요한 모듈들을 pip를 통해 모두 다운로드 받았다면 다음 코드를 실행하여 게임을 실행합니다.

```
python maingame.py
```

## How to play?
* ### 게임 시작하기
##### 들어가기에 앞서
이 게임은 게임 모드에서만 openCV로 작동되며 그 외의 버튼은 모두 마우스로 작동합니다.

##### 포인터
// 가위 바위 보에 대한 설명 적으면 될 것 같아

<p align="center">
<img src="CookIndoor/demo_image/start2.png" alt="start image" width="80%" height="60%">
</p>
게임을 실행하면 시작화면에 메뉴 선택을 눌러주세요.
종료하고자 한다면 우측 하단에 있는 종료 버튼을 눌러주세요.

<p align="center">
<img src="CookIndoor/demo_image/menu1.png" alt="start image" width="80%" height="60%">
</p>
__메뉴를 선택하세요__
4가지의 요리 중 원하는 메뉴를 선택한 후 게임 시작하기 버튼을 눌러주세요.
메뉴를 선택하지 않을 시에는 게임 시작하기 버튼이 활성화되지 않아요. 주의해주세요.

* ### 게임 모드
게임 모드에서는 메뉴마다 다른 게임 화면이 나와요. 크게 4가지 단계로 구분할 수 있으며 각각 섞는 과정, 전자레인지 돌리는 과정, 자르는 과정, 프라이팬으로 조리하는 과정, 냄비로 끓이는 과정이 있어요.

1. #### 섞기
<p align="center">
<img src="CookIndoor/image/explanation/stir_ex.PNG" alt="stir image" width="80%" height="60%">
</p>

1. #### 전자레인지 돌리기
<p align="center">
<img src="CookIndoor/image/explanation/micro_ex.PNG" alt="microwave image" width="80%" height="60%">
</p>

1. #### 자르기
<p align="center">
<img src="CookIndoor/image/explanation/cut_ex.PNG" alt="cut image" width="80%" height="60%">
</p>

1. #### 프라이팬
<p align="center">
<img src="CookIndoor/image/explanation/pan_ex.PNG" alt="pan image" width="80%" height="60%">
</p>

1. #### 냄비
<p align="center">
<img src="CookIndoor/image/explanation/pot.PNG" alt="pot image" width="80%" height="60%">
</p>
냄비는 끓이는 과정을 나타내기 위해 추가한 장면으로 자동으로 넘어가요.

## Demo video
