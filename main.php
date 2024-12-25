<?php
include 'connect.php';

if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $mobile = $_POST['mobile'];
    $password = $_POST['password'];
    $role_id = $_POST['role'];

    $sql = "insert into `users`(name,email,mobile,password,role_id) values ('$name','$email','$mobile','$password','$role_id')";
    $result = mysqli_query($conn, $sql);

    if ($result) {
        header('location:display.php');
    } else {
        die("Error updating record: " . $conn->error);
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Add User</title>
</head>
<body>
    <div class="container">
        <h2>ADD USER</h2>
        <form method="post">
            <div class="form-group">
                <label>Name</label>
                <input type="text" name="name" required>
            </div>
            <div class="form-group">
                <label>Email</label>
                <input type="email" name="email" required>
            </div>
            <div class="form-group">
                <label>Mobile</label>
                <input type="text" name="mobile" required>
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" name="password" required>
            </div>
            <div class="form-group">
                <label>Role</label>
                <select name="role" required>
                    <?php
                    include 'connect.php';
                    $roles = mysqli_query($conn, "SELECT * FROM user_roles");
                    while ($role = mysqli_fetch_assoc($roles)) {
                        echo "<option value='{$role['id']}'>{$role['role_name']}</option>";
                    }
                    ?>
                </select>
            </div>
            <button type="submit" name="submit">Add User</button>
        </form>
    </div>
</body>
</html>
