## 專題研究-生物資訊暨生物統計核心實驗室 16srRNA_platform
以微生物分析軟體 QIIME2 [1] 為基礎，EasyMap [2] 開發了方便使用者操作的視覺化介面作為分析平台。本文介紹的平台延續 EasyMap 的流程，除了既有的 LefSe [3] 分析工具用來計算 LDA (Linear discriminant analysis) 分數，此平台以 django 為框架，新增 Ancom [4]、Ancom-BC [5] 兩同樣是分析微生物組間差異物種的工具供使用者選擇，並產生視覺化的結果。

須下載 django、QIIME2、LefSe 等套件
