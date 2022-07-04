
## 1) [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression) [(선형 회귀)](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%98%95_%ED%9A%8C%EA%B7%80), [Linear Combination](https://en.wikipedia.org/wiki/Linear_combination) [(선형 결합)](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%98%95_%EA%B2%B0%ED%95%A9)
$h_\theta(x)=\theta_0+\theta_1x_1+\theta_2x_2+\cdots+\theta_nx_n$

### [Cost Function](https://en.wikipedia.org/wiki/Cost_function) **[(비용 함수, 손실 함수)](https://ko.wikipedia.org/wiki/%EC%86%90%EC%8B%A4_%ED%95%A8%EC%88%98)**

- 예측 값과 실제 값의 **차이**를 기반으로 모델의 성능(정확도)을 판단하기 위한 함수
- Linear regression의 경우 Mean Squared error function (평균 제곱 오차 함수) 활용

  → MSE(Cost)가 최소가 되도록 하는 $\theta$ (parameter, a & b)를 찾아야함.
$(y=ax+b)$


### [Gradient Descent Algorithm](https://towardsdatascience.com/gradient-descent-algorithm-a-deep-dive-cf04e8115f21) **[(경사 하강법)](https://ko.wikipedia.org/wiki/%EA%B2%BD%EC%82%AC_%ED%95%98%EA%B0%95%EB%B2%95)**

- Cost function 값을 최소로 만드는 $\theta$를 찾아나감
- Cost function의 Gradient에 상수를 곱한 것을 빼서 $\theta$를 조정

  → Cost function 에서 경사가 아래로 되어있는 방향으로 내려가서 Cost가 최소가 되는 지점을 찾는다. 어느 방향으로 $\theta$를 움직이면 Costs 값이 작아지는지 **현재 $\theta$ 위치에서 Cost 함수를 미분하여 판단**
  
## 2) Classification

### [Logistic Regression](https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc) [(로지스틱 회귀)](https://ko.wikipedia.org/wiki/%EB%A1%9C%EC%A7%80%EC%8A%A4%ED%8B%B1_%ED%9A%8C%EA%B7%80)

이진 분류 (Binary classification) 문제 해결을 위한 모델

- **[Sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) [(시그모이드 함수)](https://ko.wikipedia.org/wiki/%EC%8B%9C%EA%B7%B8%EB%AA%A8%EC%9D%B4%EB%93%9C_%ED%95%A8%EC%88%98) 이용하여 기본적으로 특정 Input data가 양성 Class에 속할 확률을 계산**
- Sigmoid function의 정확한 $y$값을 받아 양성일 확률을 예측하거나, 특정 cutoff (Threshold or Dicision boundary)를 넘는 경우 양성, 그 외$(1-y)$에는 음성으로 예측할 수 있음
- **성능 지표**로 *Mean Squared Error*가 아닌 **분류를 위한 Cost function인 [Cross-entropy](https://en.wikipedia.org/wiki/Cross_entropy) 를 활용**
- [Cross-Entropy Loss Function](https://towardsdatascience.com/cross-entropy-loss-function-f38c4ec8643e)

### [Softmax Algorithm](https://deepai.org/machine-learning-glossary-and-terms/softmax-layer) [(소프트맥스 알고리즘)](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EB%A7%A5%EC%8A%A4_%ED%95%A8%EC%88%98)

다중 클래스 분류 (Multi-class/Multinomial classification) 문제를 위한 알고리즘 (일종의 함수)
- 모델의 Output을 **각 클래스에 소속될 확률에 해당하는 값들의 벡터로 변환**해준다.
- 츨력은 항상 **0 ~ 1** 사이의 실수 값
- 출력의 총합은 항상 **1**  *(이렇기 때문에 확률로 해석할 수 있음)*
- Logistic regression을 변형/발전시킨 방법
- 차원에 영향을 미치지 않음

### SVM

### Decision Tree

### Random Forest

#### Ensemble

### Boosted Decision Tree

### Boosting Algorithm

#### (1) AdaBoost (adaptive Boosting) (1995)

#### (2) Gradient Boosting, GBM (2012)

#### (3) XGBoost (Extreme Gradient Boosting) (2016)
