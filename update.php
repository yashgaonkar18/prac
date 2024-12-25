<?php
include 'connect.php';

$id = $_GET['id'];
$sql = "SELECT * FROM users WHERE id=$id";
$result = mysqli_query($conn, $sql);
$user = mysqli_fetch_assoc($result);

if (isset($_POST['submit'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $mobile = $_POST['mobile'];
    $password = $_POST['password'];
    $role_id = $_POST['role'];

    $sql = "UPDATE users SET name='$name', email='$email', mobile='$mobile', password='$password', role_id=$role_id WHERE id=$id";
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
    <title>Update User</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>UPDATE USER</h2>
        <form method="post">
            <div class="form-group">
                <label>Name</label>
                <input type="text" name="name" value="<?= $user['name'] ?>" required>
            </div>
            <div class="form-group">
                <label>Email</label>
                <input type="email" name="email" value="<?= $user['email'] ?>" required>
            </div>
            <div class="form-group">
                <label>Mobile</label>
                <input type="text" name="mobile" value="<?= $user['mobile'] ?>" required>
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" name="password" value="<?= $user['password'] ?>" required>
            </div>
            <div class="form-group">
                <label>Role</label>
                <select name="role" required>
                    <?php
                    $roles = mysqli_query($conn, "SELECT * FROM user_roles");
                    while ($role = mysqli_fetch_assoc($roles)) {
                        echo "<option value='{$role['id']}' >{$role['role_name']}</option>";
                    }
                    ?>
                </select>
            </div>
            <button type="submit" name="submit">Update User</button>
        </form>
    </div>
</body>
</html>
