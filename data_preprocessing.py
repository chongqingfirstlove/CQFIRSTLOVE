import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path, label_column='企业类型代码'):
    # 读取Excel文件
    data = pd.read_excel(file_path, engine='openpyxl')

    # 删除非数值类型的列
    non_numeric_columns = ['证券代码', '证券简称', '年份', '企业类型']
    data = data.drop(non_numeric_columns, axis=1)

    # 处理缺失值，用每列均值填充数值列
    data.fillna(data.mean(numeric_only=True), inplace=True)

    # 检查标签列是否存在
    if label_column not in data.columns:
        raise ValueError(f"数据文件中必须包含名为'{label_column}'的列作为分类标签，当前列名为：{data.columns.tolist()}")

    # 分离特征和标签
    X = data.drop(label_column, axis=1).values
    y = data[label_column].values

    # 将标签中的2转换为0（因为代码为1表示ST，2表示非ST，这里把非ST表示为0）
    y = [1 if val == 1 else 0 for val in y]

    # 数据标准化
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y, scaler