### Perceptron

Biological Neuron을 본따 만든 알고리즘 하나의 단위

초기 형태의 인공신경망 구조. Activation function으로 Step function을 씌운것 (threshold = $\theta_j$)

다수의 입력으로부터 하나의 결과를 내보내는 알고리즘

- **[출처] [딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)**
    
    인공 신경망은 수많은 머신 러닝 방법 중 하나입니다. 하지만 최근 인공 신경망을 복잡하게 쌓아 올린 딥 러닝이 다른 머신 러닝 방법들을 뛰어넘는 성능을 보여주는 사례가 늘면서, 전통적인 머신 러닝과 딥 러닝을 구분해서 이해해야 한다는 목소리가 커지고 있습니다. 딥 러닝을 이해하기 위해서는 우선 인공 신경망에 대한 이해가 필요한데, 여기서는 초기의 인공 신경망인 퍼셉트론(Perceptron)에 대해서 이해합니다.
    
    **퍼셉트론(Perceptron)은 프랑크 로젠블라트(Frank Rosenblatt)가 1957년에 제안한 초기 형태의 인공 신경망으로 다수의 입력으로부터 하나의 결과를 내보내는 알고리즘입니다.** 퍼셉트론은 실제 뇌를 구성하는 신경 세포 뉴런의 동작과 유사한데, 신경 세포 뉴런의 그림을 먼저 보도록 하겠습니다. 뉴런은 가지돌기에서 신호를 받아들이고, 이 신호가 일정치 이상의 크기를 가지면 축삭돌기를 통해서 신호를 전달합니다.
    
    다수의 입력을 받는 퍼셉트론의 그림을 보겠습니다. 신경 세포 뉴런의 입력 신호와 출력 신호가 퍼셉트론에서 각각 입력값과 출력값에 해당됩니다.
    
    ![https://wikidocs.net/images/page/24958/%ED%8D%BC%EC%85%89%ED%8A%B8%EB%A1%A01.PNG](https://wikidocs.net/images/page/24958/%ED%8D%BC%EC%85%89%ED%8A%B8%EB%A1%A01.PNG)
    
    $x$는 입력값을 의미하며, $w$는 가중치(Weight), $y$는 출력값입니다. 그림 안의 원은 인공 뉴런에 해당됩니다. 실제 신경 세포 뉴런에서의 신호를 전달하는 축삭돌기의 역할을 퍼셉트론에서는 가중치가 대신합니다. 각각의 인공 뉴런에서 보내진 입력값 x는 각각의 가중치 w와 함께 종착지인 인공 뉴런에 전달되고 있습니다.
    
    각각의 입력값에는 각각의 가중치가 존재하는데, 이때 가중치의 값이 크면 클수록 해당 입력 값이 중요하다는 것을 의미합니다.
    
    각 입력값이 가중치와 곱해져서 인공 뉴런에 보내지고, 각 입력값과 그에 해당되는 가중치의 곱의 전체 합이 임계치(threshold)를 넘으면 종착지에 있는 인공 뉴런은 출력 신호로서 1을 출력하고, 그렇지 않을 경우에는 0을 출력합니다. 이러한 함수를 계단 함수(Step function)라고 하며, 아래는 그래프는 계단 함수의 하나의 예를 보여줍니다.
    
    ![https://wikidocs.net/images/page/24987/step_function.PNG](https://wikidocs.net/images/page/24987/step_function.PNG)
    
    이때 계단 함수에 사용된 이 임계치값을 수식으로 표현할 때는 보통 세타(Θ)로 표현합니다. 식으로 표현하면 다음과 같습니다.
    
    위의 식에서 임계치를 좌변으로 넘기고 편향 $b$ (bias)로 표현할 수도 있습니다. 편향 $b$ 또한 퍼셉트론의 입력으로 사용됩니다. 보통 그림으로 표현할 때는 입력값이 1로 고정되고 편향 $b$ 가 곱해지는 변수로 표현됩니다.
    
    이 책을 포함한 많은 인공 신경망 자료에서 편의상 편향 b가 그림이나 수식에서 생략되서 표현되기도 하지만 실제로는 편향 b 또한 딥 러닝이 최적의 값을 찾아야 할 변수 중 하나입니다.
    
    뒤에서 배우겠지만 이렇게 **뉴런에서 출력값을 변경시키는 함수를 활성화 함수(Activation Function)**라고 합니다. **초기 인공 신경망 모델인 퍼셉트론은 활성화 함수로 계단 함수를 사용**하였지만, **그 뒤에 등장한 여러가지 발전된 신경망들은 계단 함수 외에도 여러 다양한 활성화 함수를 사용하기 시작했습니다. 사실 앞서 배운 시그모이드 함수나 소프트맥스 함수 또한 활성화 함수 중 하나입니다.**
    
    퍼셉트론을 배우기 전에 로지스틱 회귀를 먼저 배운 이유도 여기에 있습니다. 퍼셉트론의 활성화 함수는 계단 함수이지만 여기서 활성화 함수를 시그모이드 함수로 변경하면 방금 배운 퍼셉트론은 곧 이진 분류를 수행하는 로지스틱 회귀와 동일함을 알 수 있습니다.
    
    다시 말하면 로지스틱 회귀 모델이 인공 신경망에서는 하나의 인공 뉴런으로 볼 수 있습니다. 로지스틱 회귀를 수행하는 **인공 뉴런과 위에서 배운 퍼셉트론의 차이는 오직 활성화 함수의 차이**입니다.
    

### **Deep Neural Network (DNN)**
은닉층이 2개 이상인 신경망 = **심층 신경망(Deep Neural Network, DNN)**
심층 신경망은 다층 퍼셉트론만 이야기 하는 것이 아니라, 여러 변형된 다양한 신경망들도 은닉층이 2개 이상이 되면 심층 신경망이라고 합니다.

### GoogLeNet
2014년도 ILSVRC(ImageNet Large Scale Visual Recognition Challenge)에서 우승한 CNN 네트워크
Inception이라는 개념의 네트워크들 중 하나이고 따라서 GoogLeNet = Inception-v1와 같은 모델임
인공 신경망에서 마지막 1-2 layer만 떨구고 Frozen $\theta$ 하고, 마지막 부분에 새로운 layer 1-2개 추가하여 (new $\theta$) 우리 목적에 맞게 조정하여 fine tuning 하여 학습시켜준다.

### **Transfer learning (전이학습)**
이미 학습이 완료되어있는 인공신경망 (기존의 지식)을 가져와서 활용할 수 있음 

### ML vs. DL
> 전통적인 머신러닝
>
>- **Feature Engineering & Feature Selection (Manual)**
>- 처음에 손은 많이 가지만, 성능을 향상시킬 때 수월함
>
>
> **딥러닝**
>
>- **Feature Extraction (with neural network)**
>- **E2E (End-to-end) Learning**
>- 데이터 잔뜩 밀어넣어주면 신경망 내부에서 자체적으로 데이터의 중요한 Feature를 찾거나 구성
>
>---
>
>- 처음에 손은 많이 안가지만 (데이터 밀어넣고 끝), 성능을 향상시켜나갈때가 어려움 (overfitting 처리 등…)
>- 선입견을 배제하는 장점
>
>---
>
>- 데이터의 양이 많이 필요함!! (***Large amounts***)
>- 최소 class당 수백장… 필요
>- 논문 *10,000 단위* 이상
>- 사람 단위로 뽑아내려면 *50k 단위* 이상의 데이터가 있어야함
>→ **data augmentation**을 통해서 어느정도 해결할 수 있음 (아직은 손으로 하고 있지만, 컴퓨터에게 맡길 수도 있음)
>- ***+ Labeled data*** 이어야 함!
>

### Single-Layer Perceptron (SLP, 단층 퍼셉트론)
두가지 연산을 적용하여 출력값 계산

### 1) **Linear combination**
**데이터와 $θ$ 들의 Linear combination (선형 결합)을 계산 (합 & 곱)** `Scalar값 하나 나옴`  

$$
\theta_0+\theta_1x_1+\theta_2x_2+ \cdots +\theta_nx_n
$$

**+**   *(→ 아무리 layer를 쌓더라도 선형회귀로만 나와서 선형회귀를 벗어나지 못함.
           그래서 활성화 함수가 필요하다)*

### 2) **Activation function (활성화 함수)**

$$
g(\sum_i{ \theta_ix_i})
$$

비선형 함수(Non-linear function)
⇒  다음 layer로 얼마나 넘겨줄지 결정!
- Step function
- Sigmoid Function을 Activation function으로 쓰게 된다면, 양극단을 제외하고 대부분 0이 아닌 기울기가 존재한다.
    그러나 기울기의 최대값이 0.25이기 때문에 한계가 있음. 그래서 시그모이드 함수도 잘 쓰지 않고 이후 활성화 함수로 나온것이 ReLU function이다.
- tanh (Hyperbolic Tangent) function
    시그모이드 함수의 범위 [0, 1]를 [-1, 1]로 -1까지 내림
- ReLU (Rectified Linear Unit) Function을 사용하면 미분 결과값이 0 또는 1 *(사실상 1)* 이므로 에러(MSE)가 과거로 잘 살아서 돌아갈 수 있다.
- ELU (Exponential LU) : x값이 음수인 부분이 곡선으로 되어있음
- PreLU (Parametric ReLU) : Leaky ReLU 기준으로 $\alpha$ 값을 학습의 대상이 되는 parameter $\theta$로 처리함
⇒ 현재 일반적으로 ReLU 계열이 많이 쓰이고 있고,  자연어처리에서는 Tanh 계열 쓰임

<br>

### Multi-Layer Perceptron (MLP, 다층 퍼셉트론) ≈ ANN 인공신경망
- 하나의 Perceptron으로는 XOR 문제를 해결할 수 없었음
- Layer가 쌓이면 쌓일 수록 복잡한 함수선(결정 경계)을 만들어 낼 수 있게 되었다.
    Non-linear Activation function & Multi-Layer
    점점 엄청나게 복잡하게 그려갈 수 있지만 그럴수록 Overfitting될 가능성이 커진다.
    
💡 **전통적인 머신러닝은 Feature와의 싸움이고, 딥러닝은 Overfitting과의 싸움이다!**


### Artificial Neural Network (ANN)
Perceptron을 모은 Layer를 깊이 방향으로 쌓아나가면서 복잡한 모델을 만들어내어 보다 더 어려운 문제를 풀어낼 수 있음
- Input Layer 입력층
- Hidden Layer 은닉층
    - Hidden Layer == Learnable Kernel** (학습 가능한 커널), Hidden layer로 대부분 ReLU 사용함
- Output Layer 출력층
    - 결과값을 그대로 받아 Regression
    - 2진 분류의 경우,
        - **Sigmoid** (y값이 양성 클래스일 확률)를 거쳐 → **Binary Classification** ($y$값 = Class 1, 나머지 ($1-y$) = Class 0)
        - **Softmax** 를 거쳐 → **K-Class Classification** (Class 0 or Class 1)   

**인공신경망에서는 항상 $θ$ (Theta, parameters)가 주인공이다!**


### Deep Neural Network (DNN)
MLP 중에서도 Hidden Layer가 2개 이상인 인공신경망


### Forward Propagation (Feedforward Neural Network)
Input Layer에서 시작하여 순방향으로 계산해 나아가며 Output Layer까지 값을 전파해나가는 신경망

***Hyper Parameters***  
- Layers 개수
- Neurons 개수
- Activation function

***Feedforward 신경망의 학습*** 
원하는 결과를 얻기 위해 **뉴런 사이의 적당한 가중치 $\theta$들을 알아내는 것**  
→ Model의 Output과 실제 정답의 차이를 바탕으로 Cost function을 구성하고, Cost를 낮추도록 **Gradient Descent**를 적용하여 최적의 가중치 $\theta$를 찾아감

### Back Propagation Algorithm (오차 역전파 알고리즘) == 신경망의 효율적인 학습 방법
학습된 출력 값과 실제 값과의 차이인 오차를 계산하여 Feedforward 반대인 역방향으로 전파(Propagation)하는 알고리즘
- Multi-Layer Perceptron으로 XOR 문제 해결 → 그러나 Layer 복잡해질수록 연산이 복잡해져서 현실적으로 매우 비효율적
    
이 문제를 해결하기 위해 **Back propagation** 알고리즘이 도입됨
    - Forward 방향으로 한번 연산 
    → 결과값 (오차 발생, Cost) 나옴 (cost func: `틀린 정도의 기울기`)  
    → Cost를 역방향(Backward)으로 전달해가면서 Parameter Update!  
      (각 weight 마다 Cost에 미치는 영향을 계산해서 Cost 줄이도록 weight, bias update)
    
> 모델이 `틀린 정도`를 `역방향`으로 전달하여 ‘미분’하고 곱하고 더하는 것을 반복하여 Parameter($\theta$)를 갱신한다. (Reverse Feed-forward)
> 

### Vanishing Gradient
- Layer가 깊어질수록 앞선 오차 값이 역방향으로 뒤까지 전달되지 않는 문제 발생
- 미분의 최대값이 0.25인 Sigmoid를 적용시 역방향으로 0.25보다 작은 값을 곱하고 더해가면서 오차값이 사라져 버림
- 이로 인해 학습 속도가 크게 저하되거나 학습이 중지됨

  ⇒ ReLU function으로 Activation function을 적용하면서 해결됨


## Neural Network Optimization

### 1) Weight Initialization (가중치 초기화)

Parameter(θ) 초기값에 따라 학습 결과 달라질 수 있기때문에 Parameter(θ)를 random하게 초기화하는 것은 좋지 않을 수 있다. 
→ Perceptron의 Linear combination 결과값이 너무 커지거나 작아지지 않게 해주려는 것
→ Vanishing gradient 혹은 Exploding gradient 문제를 줄일 수 있음
- **Xavier Initializaton** (with Sigmoid or tanh): 보통 딥러닝 라이브러리에 Default parameter로 setting 되어있음
    - 표준편차가 $\sqrt{\frac{1}{n}}$  인 정규분포 따르도록 가중치 초기화 (n = # of nodes of previous layer)
    - 앞에 있는 perceptron (# of nodes) 개수가 많아질 수록 Parameter($θ$)값을 작게 줄여준다.
    - 
- **He initialization** (with ReLU)
    - 활성화 함수가 ReLU 함수일 때 적용
    - 표준편차가 $\sqrt{\frac{2}{n}}$  인 정규분포 따르도록 가중치 초기화

### 2) Weight regularization (가중치 규제) - L1 규제 & L2 규제
기존 Gradient Descent 계산 시 y축에 위치했던 Cost function은 Training data에 대해 모델이 발생시키는 Error값의 지표이다.
- 모델이 복잡해질수록 θ 개수가 늘어나고 |θ| 커지는 경향성이 있음
  따라서 MSE(손실함수)를 그대로 활용하는 것이 아니라, Regularization Term을 더해서 `New Cost function; J(θ)`을 만든다.

**Lambda** : Regularization Rate (Hyper-params), 정규화율
- 스칼라 값
- 정규화 함수의 상대적 중요도를 지정해준다.
- 정규화율을 높이면 과적합 감소하지만 모델 정확성 떨어질 수 있음 (Underfitting)
- θ의 개수가 아주 많은 신경망은 정규화율을 아주 작게 주기도 함
- 절대값 그래프의 너비 or 원의 크기를 결정해줌 (lambda ↑ 이면 원의 크기 ↓)

- **L1 regularization [Lasso]**
    
    $$
    \lambda \sum_{i=1}^{k} |\theta|
    $$
    
    크게 중요하지 않은 $x$ data (column)의 가중치($\theta$)를 정확히 $0$으로 만들어주어 모델에서 해당 특성을 배제하도록 함 ( ⇒ Feature selection 효과 )
    
- **L2 regularization [Ridge]**
    
    $$
    \lambda \sum_{i=1}^{k} \theta^2_i
    $$
    
    전반적으로 Overfitting을 줄여준다. 큰 값을 가진 가중치($\theta$)를 더욱 제약하는 효과가 있음
    
- **Elastic-Net :** Ridge & Lasso 모두 적용한 Cost Function


### 🗺️ [Choosing the right estimator](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)


### 3)  Advanced gradient descent algorithms

### - **Full-Batch Gradient Descent**
- 모든 Training data인 전체데이터 다 넣고 진행하는거라 엄~~청 느림
- 가중치 초기화 결과에 따라 Global minimum이 아닌 Local minimum으로 수렴할수도 있음

### - **Stochastic Gradient Descent (SGD, 확률적 경사하강법)**
- 하나의 Training data (Batch size=1)마다 Cost 를 계산, Gradient Descent 바로 적용하여 weight update가 빠름
- 신경망 성능이 들쑥날쑥 변하여 Cost값이 안정적으로 줄어드는것이 아니라서 안정성이 다소 떨어진다 (실용적이지 않음)
- 최적의 Learning rate 구하기 위해 일일이 튜닝하고 수렴조건(early-Stop)을 조정해야함

### - **Mini-Batch Stochastic Gradient Descent (Mini-Batch SGD)**
Training data에서 **일정한 크기 (== Batch size)의 데이터를 선택**하여 Cost function 계산 및 Gradient descent 적용
- 일반 Gradient Descent와 Stochastic Gradient Descent (SGD) 기법의 단점을 보완하고 장점을 취한다.
- 설계자 의도에 따라 속도&안정성을 동시에 관리할 수 있고 GPU 기반의 효율적인 병렬 연산이 가능해진다.
- 이 기법이 가장 보통의 방식이 됨

### Gradient Descent Method or Momentum Optimize  
- **Adam (Adaptive Moment Estimation) Optimizer**
    - Momentum과 AdaGrad/RMSProp의 장점을 조합
    - Adaptive learning rate가 적용되어 learning rate 탐색 필요성이 줄어듦
- **RAdam (Rectified-Adam)**

→ 계속 발전하고 있다…… 😮

## Avoiding overfitting

### 1) Dropout
```Python
tf.keras.layers.Dropout(0.5)
```
- 신경망에 적용할 수 있는 효율적인 Overfitting 회피 방법 중 하나 (무조건 먼저 적용하지는 않음)
- Training을 진행할 때 매 Batch 마다 Layer 단위로 일정 비율만큼의 Neuron을 꺼뜨리는 방식으로 적용
- Test / Inference 단계에는 Dropout을 걷어내어 전체 Neuron이 살아있는 채로 Inference 진행해야 함
- Random하게 Neuron을 꺼트려 학습을 방해함으로써 모델 학습이 Training data에 편향되는 것을 막아주는 것이 핵심
- 동일한 데이터에 대해 매번 다른 모델을 학습시키는 것과 같은 효과를 발생시켜 일종의 Model ensemble 효과를 얻을 수 있음
- 전체적으로 Overfitting을 줄여주어 Test data에 대한 error를 더욱 낮출 수 있게 해줌
- 가중치 값이 큰 특정 Neuron의 영향력이 커져 다른 Neuron들의 학습 속도에 문제를 발생시키는 Co-adaptation을 회피할 수 있게 함
- Alexnet 경우, 마지막 1-2개 Fully-connected layer에 dropout 적용시킴 (`p==0.5` or `p==0.8` 정도)
