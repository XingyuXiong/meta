## 账户模块

----

## 主模块

'POST /api/main/get_sim_pic'

对于指定图片，点击访问与其相似的图片，请求参数

* 'id'（图片id）
* 'max'（返回图片数量最大值）

返回一个列表，其中每一项为

* 'id'
* 'rate'（与给定图片的相关度）（非必要）
