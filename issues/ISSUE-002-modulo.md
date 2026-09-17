# ISSUE-002: 为计算器模块添加取模运算功能
- 编号：ISSUE-002 / 状态：open / 优先级：P1 / 认领人：待认领 / 依赖：无
## 目标
新增 modulo(a, b)：返回 a mod b，除零显式报错。
## 验收标准（必须可测试、可机器判定）
- [ ] AC1: modulo(7, 3) 返回 1.0
- [ ] AC2: modulo(-7, 3) 返回 1.0（Python 语义）
- [ ] AC3: modulo(7, 0) 抛出 ValueError
- [ ] AC4: python -m pytest tests/test_calculator_modulo.py -q 全部通过
- [ ] AC5: lint 无新增告警
## 边界与非目标
- 做：新增 src/calculator_modulo.py 与测试文件
- 不做：不修改 src/calculator.py；不引入 math.fmod
