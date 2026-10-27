$\begin{aligned} &\texttt{for} (\texttt{j} = 1;\texttt{j} <= \texttt{n};\texttt{j}++)\\ &\quad \texttt{count++};\\ \end{aligned}$ A. $O(\log_{2}n)$ B. $O ( n )$ C. $O ( n \log _ { 2 } n )$ D. $O(n^{2})$

14.【2017统考真题】下列函数的时间复杂度是（）。int func(int n){int i=0, sum=0; while(sum<n) sum += ++i; return i;} A. O(logn) B. $O ( n ^ { 1 / 2 } )$ C. O(n) D. O(nlogn)

15.【2019统考真题】设n是描述问题规模的非负整数，下列程序段的时间复杂度是()。x=0; while (n>=(x+1)\*(x+1)) x=x+1; A. O(logn) B. $O ( n ^ { 1 / 2 } )$ C. O(n) D. $O ( n ^ { 2 } )$

16.【2022统考真题】下列程序段的时间复杂度是（）。int sum=0; for $\begin{array} { c } { \mathtt { ( i n t \_ i = 1 ; i < n ; i > = 2 ) } } \\ { \mathtt { f o r ( i n t \_ j = 0 ; j < i ; j ++ ) } } \\ { \mathtt { s u m ++ ; } } \end{array}$ A. O(logn) B. O(n) C. O(nlogn) D. $O(n^{2})$

## 二、综合应用题

01. 分析以下各程序段，求出算法的时间复杂度。① $\begin{aligned}& if  = 1;  k  = 0; \\&\quad \mathsf{whi.1e (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (i<n-1) (n-2) (n-2) (n-2) (n-1) (n-2) (n-2) (n-1) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-2) (n-1 (n-1 -1) (n-1 ) (n-1 ) (n-2) (n-2) (n-1 (n-1 -1 ) (n-1 ) (n- 2) (n- 2) (n- 2) (n- 2) (n- 2) (n- 2) (n- 2 ) (n- 2 ) (n (n- 2 ) (n- 2 ) (n - 2 ) (n - 2 ) (n - 2 ) (n ) (n - 2 ) (n - 2 ) (n ) (n - 2 ) (n - 2 ) (n ) (n - 2 ) (n ) (n - 2 ) (n ) (n - 2 ) (n - 2 ) (n ) (n - 2 ) (n ) (n - 2 ) ( n ) ( n - 2 ) ( n ) ( n - 2 ) ( n ) ( n ) ( n - 2 ) ( n ) ( n ) ( n ( n ) - 2 ) ( n ( n ) ) ( n ) ( n ) ( n ( n ) ) ( ( n ) ) ( 2 ) ( ) ( ) ( ) ( ) ( 2 ) ( ) = 2 ( ) ( ) ( ) ( ) ) ( ) ( 2 ) ( ) ( ) = ( } & = & = & = 1 1 ( = 1 1 , , , 1 , = 1 , 1 , , 1 , 1 , = 1 , , 1 , , 1 , : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :  \end{aligned}$ $\begin{aligned} &\begin{aligned}\\ & ) \\& \begin{aligned}\\ & \boldsymbol{y} = & 0\\ &\end{aligned},\\ &\end{aligned}\\ \end{aligned}$ ② $\begin{aligned} &y = 0 ; \quad\\ &\text { while } \left( (y + 1) \star (y + 1) <= n \right) ; \quad\\ &y = y + 1 ;\\ \end{aligned}$ ③ $\begin{aligned}& for   (\mathtt{i} = 0; \mathtt{i} < \mathtt{n}; \mathtt{i}++) \\&\quad  for   (\mathtt{j} = 0; \mathtt{j} < \mathtt{m}; \mathtt{j}++) \\&\quad \quad \mathtt{a}   [\mathtt{i}]   [\mathtt{j}] = 0;\end{aligned}$

## 1.2.4 答案与解析

## 一、单项选择题

## 01. B

本题是中山大学往年真题，题目没有问题，考查的是算法的定义。程序不一定满足有穷性，如死循环、操作系统等，而算法必须有穷。算法代表对问题求解步骤的描述，而程序则是算法在计算机上的特定实现。不少读者认为C也对，它只是算法的必要条件，不能成为算法的定义。

02. C

时间复杂度为 $O(n^{2})$ ，说明算法的时间复杂度T(n)满足 $T(n) \leq c n^{2}$ (其中 $c$ 为比例常数)，即$T(n) = O(n^2)$ ，时间复杂度T(n)是问题规模n的函数，其问题规模仍然是n而不是 $n^{2}$