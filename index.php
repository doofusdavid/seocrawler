<?php
require_once("./header.php");
?>

<div class="content">
<form action="index_proc.php" method="post">
    <p>
        <input type="text" name="login" id="login" placeholder="Login">
    </p>
    <p><input type="password" name="password" id="password" placeholder="Password"></p>
    <p><input type="text" name="url" id="url" placeholder="URL To Scan"></p>
    <input type="submit" value="Log In">
</form>
</div>

<script src="./js/index.js"></script>
<?php
require_once("footer.php");