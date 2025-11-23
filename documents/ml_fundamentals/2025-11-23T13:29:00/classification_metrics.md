# **머신러닝 기초: 지도 학습 (Classification) 핵심 평가 지표**

ML 엔지니어 채용 과정에서는 모델의 성능을 **정확하게 평가하고 비즈니스 목표에 맞게 해석**하는 능력을 중요하게 평가합니다. 다음 개념들을 명확히 이해하고 있어야 합니다.

## **1\. 혼동 행렬 (Confusion Matrix)**

분류 모델의 성능을 시각적으로 나타내는 표입니다. 모든 평가 지표의 기본이 되므로, 각 항목이 무엇을 의미하는지 정확히 알아야 합니다.

| 실제값(Actual) / 예측값(Predicted) | Positive로 예측 (P') | Negative로 예측 (N') |
| :---- | :---- | :---- |
| **실제 Positive (P)** | **TP (True Positive)** | **FN (False Negative)** |
| **실제 Negative (N)** | **FP (False Positive)** | **TN (True Negative)** |

* **TP (True Positive):** 실제 Positive인 것을 Positive로 **정확히** 예측 (올바른 예측)
* **FN (False Negative):** 실제 Positive인 것을 Negative로 **잘못** 예측 (놓침, Type II Error)
* **FP (False Positive):** 실제 Negative인 것을 Positive로 **잘못** 예측 (오탐, Type I Error)
* **TN (True Negative):** 실제 Negative인 것을 Negative로 **정확히** 예측

## **2\. 주요 평가 지표**

### **A. 정확도 (Accuracy)**

가장 직관적이지만, 데이터 불균형(Imbalanced Data) 문제에서 모델의 성능을 왜곡할 수 있습니다.

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$


### **B. 정밀도 (Precision)**

모델이 'Positive'라고 예측한 것 중에서 **실제 Positive인 비율**. FP를 줄이는 것이 중요한 상황(예: 스팸 메일 필터링)에서 중요합니다.

$$\text{Precision} = \frac{TP}{TP + FP}$$

### **C. 재현율 (Recall, Sensitivity)**

실제 'Positive'인 것 중에서 **모델이 Positive라고 정확히 예측한 비율**. FN을 줄이는 것이 중요한 상황(예: 암 진단, 사기 탐지)에서 중요합니다.

$$Recall = \frac{TP}{TP + FN}$$

### **D. F1-Score**

정밀도와 재현율의 조화 평균(Harmonic Mean)입니다. 두 지표가 모두 중요하며, 어느 한 쪽으로 치우치지 않는 균형 잡힌 성능이 필요할 때 사용됩니다.

$$F1-Score = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$$

## **3\. ROC Curve와 AUC**

### **A. ROC Curve (Receiver Operating Characteristic Curve)**

\*\*TPR (True Positive Rate)\*\*과 \*\*FPR (False Positive Rate)\*\*의 변화를 그래프로 나타낸 것입니다. 모델의 \*\*임계값(Threshold)\*\*을 변경할 때마다 TPR과 FPR이 어떻게 변하는지 보여줍니다.

* **TPR (True Positive Rate) = Recall:** 실제 Positive 중 맞춘 비율 ($$\frac{TP}{TP + FN}$$
  )
* **FPR (False Positive Rate):** 실제 Negative 중 틀린 비율 ($$\frac{FP}{FP + TN}$$
  )

A typical ROC curve showing the trade-off between TPR and FPR. The dashed line represents a random classifier (AUC \= 0.5), and a perfect classifier would go straight up to the top-left corner (0,1) then across to (1,1) (AUC \= 1).

### **B. AUC (Area Under the Curve)**

ROC Curve의 **곡선 아래 면적**을 의미하며, 모델의 **전반적인 분류 성능**을 나타냅니다. 임계값에 관계없이 모델이 임의의 Positive 샘플과 Negative 샘플을 올바르게 분류할 확률로 해석됩니다.

* **해석:** AUC 값이 1에 가까울수록 성능이 좋으며, 0.5는 무작위 분류와 같습니다.

## **4\. Precision-Recall Curve (PR Curve)**

\*\*정밀도(Precision)\*\*와 \*\*재현율(Recall)\*\*의 변화를 그래프로 나타낸 곡선입니다. 특히 **데이터 불균형이 심한(Imbalanced Data)** 경우, Positive 클래스(소수 클래스)에 대한 모델의 성능을 더 효과적으로 평가할 수 있습니다.

* **X축:** Recall (재현율)
* **Y축:** Precision (정밀도)
* **해석:** PR Curve는 일반적으로 오른쪽 위로 볼록한 형태를 띠며, 곡선이 오른쪽 상단(Precision 1, Recall 1)에 가까울수록 좋은 성능을 의미합니다. ROC AUC와 유사하게, PR Curve 아래 면적(Average Precision)을 계산하여 모델의 전반적인 성능을 평가하기도 합니다.

💡 왜 불균형 데이터셋에서 PR Curve가 더 유용할까요?
ROC Curve의 FPR은 TN(True Negative)을 포함합니다. 불균형 데이터셋에서 Negative 클래스가 압도적으로 많으면, 모델이 Negative를 모두 Negative로 예측하기만 해도 TN이 매우 커져 FPR이 낮게 유지될 수 있습니다. 이 경우 ROC Curve는 모델 성능을 과대평가할 수 있습니다. 반면 PR Curve는 Positive 클래스 예측에 집중하므로, 소수 클래스에 대한 모델의 실제 성능을 더 정확하게 반영합니다.

## **5\. 예상 객관식/단답형 질문 (Self-Test)**

1. **질문:** 광고 플랫폼에서 **CTR(클릭률) 예측 모델**의 성능을 평가할 때, Precision과 Recall 중 어떤 지표가 더 중요하며 그 이유는 무엇인가요?
   * **답변 예시:** 광고 플랫폼의 비즈니스 목표는 사용자에게 관련성 높은 광고를 노출하여 \*\*클릭(Positive)\*\*을 유도하는 것입니다. 하지만 한정된 광고 인벤토리(자리)에서 효율성을 극대화해야 합니다. 이때 \*\*Precision (광고 클릭이라고 예측한 것 중 실제 클릭)\*\*이 중요합니다. Precision이 높을수록 노출된 광고가 낭비 없이 클릭으로 이어질 확률이 높아져 광고 효율이 증대됩니다.
2. **질문:** 데이터셋이 매우 불균형(예: Positive 1%, Negative 99%)할 때, Accuracy 대신 사용해야 하는 두 가지 주요 지표를 제시하고 그 이유를 설명하세요. 추가적으로 ROC Curve와 PR Curve 중 어떤 것을 더 중점적으로 볼 것인지 그 이유와 함께 설명하세요.
   * **답변 예시:** Precision과 Recall(또는 F1-Score)을 사용해야 합니다. Accuracy는 99% Negative를 모두 Negative로 예측해도 99%가 나오기 때문에 모델의 실제 성능을 왜곡합니다. Precision과 Recall은 소수 클래스(Positive)에 대한 모델의 성능을 직접적으로 평가합니다. 불균형 데이터셋에서는 **PR Curve**를 더 중점적으로 봐야 합니다. ROC Curve의 FPR은 TN을 포함하는데, Negative 클래스가 압도적으로 많으면 TN이 커져 FPR이 낮게 유지될 수 있어 ROC Curve가 모델 성능을 과대평가할 가능성이 있습니다. PR Curve는 Positive 클래스 예측에 직접 집중하여 소수 클래스에 대한 모델의 실제 성능을 더 정확하게 반영합니다.
3. **질문:** ROC Curve에서 \*\*왼쪽 상단 코너 (0, 1)\*\*에 가까울수록 모델이 좋다고 말하는 이유는 무엇인가요?
   * **답변 예시:** 왼쪽 상단은 TPR(True Positive Rate, Recall)이 1에 가깝고, FPR(False Positive Rate)이 0에 가깝다는 의미입니다. 이는 실제 Positive를 모두 맞추면서(TPR=1), 실제 Negative를 Positive로 잘못 예측하는 실수(FPR=0)는 거의 없다는 것을 나타내므로, 가장 이상적인 분류 성능을 의미합니다.
