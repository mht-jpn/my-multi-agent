# ISSUE-001: 为计算器模块添加百分比运算功能

- 编号：ISSUE-001
- 状态：open
- 优先级：P1
- 认领人：待认领
- 依赖：无

## 背景
计算器模块目前支持四则运算，缺少百分比换算；下游报表场景需要
"求 base 的 rate%" 这一原子能力。

## 目标
新增 percent(base, rate) 函数：返回 base 的 rate 百分比数值，
非法输入显式报错。

## 验收标准（必须可测试、可机器判定）
- [ ] AC1: percent(200, 10) 返回 20.0
- [ ] AC2: percent(50, 0) 返回 0.0
- [ ] AC3: percent(200, -10) 抛出 ValueError
- [ ] AC4: python -m pytest tests/test_calculator_percent.py -q 全部通过
- [ ] AC5: lint 无新增告警

## 边界与非目标
- 做：新增 src/calculator_percent.py 与对应测试文件
- 不做：不修改 src/calculator.py；不做连乘/复利等复合运算；不做 UI

## 依赖与参考
- 相关文件：src/calculator_percent.py（新建）、tests/test_calculator_percent.py（新建）
