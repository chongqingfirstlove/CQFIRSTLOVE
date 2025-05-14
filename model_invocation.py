import pandas as pd
import joblib

# 1. 加载模型和标准化参数
model = joblib.load('bp_adaboost_model.pkl')
scaler = joblib.load('standard_scaler.pkl')

# 2. 读取新数据并预处理
new_data = pd.read_excel('exercise1.xlsx', engine='openpyxl')

# 删除非数值列（需与训练数据一致）
new_data = new_data.drop(['证券代码', '证券简称', '年份', '企业类型'], axis=1, errors='ignore')

# 填充缺失值（用每列均值）
new_data.fillna(new_data.mean(numeric_only=True), inplace=True)

# 3. 标准化处理
X_new = scaler.transform(new_data.values)

# 4. 预测ST概率
probabilities = model.predict_proba(X_new)

# 5. 输出结果
for i, prob in enumerate(probabilities):
    print(f"企业 {i+1} 的ST风险概率：{prob:.2%}")