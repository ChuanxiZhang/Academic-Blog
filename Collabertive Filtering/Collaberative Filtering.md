## 1. Introduction
  * <h4> 1. Collaborative filtering algorithm is earliest and famous recommendation algorithm.

  * <h4> 2. Usage: prediction and recommendation.
  * <h4> 3. Idea: Mining user preferences based on user's historical data
  * <h4> 4. Classification:

    * <h5> 1. User-based collaborative filtering
    * <h5> 2. Item-based collaborative filtering

## 2. User-based collaborative filtering
  * <h4> 1. Principle:
    * <h5> 1. Mining user preferences for contents of post based on historical data.
    * <h5> 2. Calculate relationship between users based on attitude sand preferences of different users for same post.
    * <h5> 3. Recommending post between user with same preferences.
          ![avatar](https://github.com/ChuanxiZhang/Academic-Blog/blob/master/Collabertive%20Filtering/diagram/user_based_collaboratIve_filtering.png?raw=true)
      1) Fig. 1: Usecase Diagram of users and posts
      (code: user_based_collaboratIve_filtering.uml)
  Reference:
  http://www.plantuml.com
  https://www.cnblogs.com/ningskyer/articles/5397750.html
  https://www.jianshu.com/p/e92a52770832

    1. Historical data: Including save, like, share, click and comment.
  2. Search Similar User:
    1. By scatter Graph
      Post 1	Post2
    User1	3.3	6.5
    User2	5.8	2.6
    User3	3.6	6.3
    User4	3.4	5.8
    User5	5.2	3.1


    We cannot directly recognize relationship among 5 users. However, after drawing a scatter plot, we can easily find user1, user3 and user4 are more close.   User 2 and user 5 are the other group.

    Reference：
    https://blog.csdn.net/u013634684/article/details/49646311
    https://blog.csdn.net/abcjennifer/article/details/19848269
    https://blog.csdn.net/You_are_my_dream/article/details/53441141
    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html
    2. By mathematical methods
    Through scatter graph is more intuitive, it can not be apply to computer coding. Therefore, there are some common mathematical methods to measure relationship.

      1) Euclidean distance

      d(x, y)=\ √((x_1−y_1 )^2+(x_2−y_2 )^2+…+(x_n−y_n )^2 )=√(∑_(i=1)^n▒〖(x_i  −y_i)^2〗)   
    Through above fomula,  we can wirte code and calculate Euclidean distance for these five users. ()
    Reference：
    https://www.jianshu.com/p/a9e94c9922c2
    http://cn.onenotegem.com/2599126723/-onenote1347541

3. Item based collaborative filtering
