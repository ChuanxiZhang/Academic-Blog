## 1. Introduction
  * <h4> 1. Collaborative filtering algorithm is earliest and famous recommendation algorithm.
  * <h4> 2. Usage: prediction and recommendation.
  * <h4> 3. Idea: Mining user preferences based on user's historical data
  * <h4> 4. Classification:
    * <h5> 1. User-based collaborative filtering
    * <h5> 2. Item-based collaborative filtering

## 2. User-based collaborative filtering
  * <h4> 1. Principle:
    * <h5> (1) Mining user preferences for contents of post based on historical data.
    * <h5> (2) Calculate relationship between users based on attitude sand preferences of different users for same post.
    * <h5> (3) Recommending post between user with same preferences.</h5>
# ![fig1](https://github.com/ChuanxiZhang/Academic-Blog/blob/master/Collabertive%20Filtering/diagram/user_based_collaboratIve_filtering.png?raw=true)
      <center>[[Source](https://github.com/ChuanxiZhang/Academic-Blog/blob/master/Collabertive%20Filtering/code/user_based_collaboratIve_filtering.uml)] Fig. 1: Usecase diagram of users and posts [1-3](#Reference_plantuml)</center>

    * <h5> (4) Historical data: Including save, like, share, click and comment.</h>

  * <h4> 2. Search Similar User:

    * <h5> (1) By scatter Graph

<center>

| User  | Post1 | Post2 |
|:---:|:---:|:---:|
| User1 | 3.3   | 6.5   |
| User2 | 5.8   | 2.6   |
| User3 | 3.6   | 6.3   |
| User4 | 3.4   | 5.8   |
| User5 | 5.2   | 3.1   |
Table 1: Quantitative score of 5 users</center>
# ![fig2](https://github.com/ChuanxiZhang/Academic-Blog/blob/master/Collabertive%20Filtering/diagram/scatter_plot.png?raw=true)
  <center>[[Source](https://github.com/ChuanxiZhang/Academic-Blog/blob/master/Collabertive%20Filtering/code/user_based_collaboratIve_filtering.uml)] Fig. 2: Scatter diagram of five users [[1-3](#Reference_plantuml)]
* 
    * <h5> (2) By mathematical methods
      * Through scatter graph is more intuitive, it can not be apply to computer coding. Therefore, there are some common mathematical methods to measure relationship.

      * <h6> 1) Euclidean distance
# ![fig2](https://github.com/ChuanxiZhang/Academic-Blog/blob/master/Collabertive%20Filtering/diagram/euclidean_distance_formula.png?raw=true)
  <center>Fig. 3: Formula of Euclidean distance[[1-3](#Reference_plantuml)]

      * Through above fomula,  we can wirte code and calculate Euclidean distance for these five users.  After calculate, the results shown as following:

<center>

| User  | Quantitative score | Normalized score|
|:---:|:---:|:---:|
| User1 & User2 | 4.6325   | 0.1775   |
| User1 & User3 | 0.3606   | 0.7350   |
| User1 & User4 | 0.7071   | 0.5858   |
| User1 & User5 | 3.8949   | 0.2043   |
| User2 & User3 | 4.3046   | 0.1885   |
| User2 & User4 | 4.0000   | 0.2000   |
| User2 & User5 | 0.7810   | 0.5615   |
| User3 & User4 | 0.5385   | 0.6500   |
| User3 & User4 | 3.5777   | 0.2184   |
| User4 & User5 | 3.2450   | 0.2355   |

[[Source](https://github.com/ChuanxiZhang/Academic-Blog/blob/master/Collabertive%20Filtering/code/euclidean_distance.py)] Table 2: Quantitative score of 5 users</center>
## 3. Item based collaborative filtering

## Reference:
<div id = "Reference_plantuml"></div>
Diagram tools: plantuml
  * [1] http://www.plantuml.com
  * [2] https://www.cnblogs.com/ningskyer/articles/5397750.html
  * [3] https://www.jianshu.com/p/e92a52770832
