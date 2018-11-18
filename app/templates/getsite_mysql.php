<?php
$q = isset($_GET["q"]) ? intval($_GET["q"]) : '';
 
if(empty($q)) {
    echo '请选择一个网站';
    exit;
}
 
$con = mysqli_connect('localhost','root','12345678');
if (!$con)
{
    die('Could not connect: ' . mysqli_error($con));
}
// 选择数据库
printf("success");
mysqli_select_db($con,"wulianwang");
// 设置编码，防止中文乱码
mysqli_set_charset($con, "utf8");
 
$sql="SELECT * FROM engineering WHERE id = '".$q."'";
 
$result = mysqli_query($con,$sql);
 
echo "<table border='1'>
<tr>
<th>ID</th>
<th>网站名</th>
<th>网站 URL</th>
<th>Alexa 排名</th>
<th>国家</th>
</tr>";
 
while($row = mysqli_fetch_array($result))
{
    echo "<tr>";
    echo "<td>" . $row['engineeringnum'] . "</td>";
    echo "<td>" . $row['engineeringname'] . "</td>";
    echo "<td>" . $row['engineeringlocation'] . "</td>";
    echo "<td>" . $row['engineeringuser'] . "</td>";
    echo "<td>" . $row['engineeringtime'] . "</td>";
    echo "</tr>";
}
echo "</table>";
 
mysqli_close($con);
?>
