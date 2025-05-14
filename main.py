from data_preprocessing import preprocess_data
from model_training import AdaboostBP
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    file_path = 'ST企业和非ST企业的合并.xlsx'
    label_column = '企业类型代码'

    # 预处理数据
    X, y, scaler = preprocess_data(file_path, label_column=label_column)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 训练模型
    model = AdaboostBP(n_estimators=10)
    model.fit(X_train, y_train)

    # 在测试集上进行预测
    y_pred = model.predict_proba(X_test)
    # 将概率转换为类别标签（这里假设概率大于0.5为正类，小于等于0.5为负类）
    y_pred_labels = [1 if prob > 0.5 else 0 for prob in y_pred]

    # 计算正确率
    accuracy = accuracy_score(y_test, y_pred_labels)
    print(f"模型在测试集上的正确率: {accuracy * 100:.2f}%")

    # 保存模型和标准化参数
    joblib.dump(model, 'bp_adaboost_model.pkl')
    joblib.dump(scaler, 'standard_scaler.pkl')

if __name__ == "__main__":
    main()