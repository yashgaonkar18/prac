<?php
include 'connect.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Users</title>
</head>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 20px;
        color: #333;
    }

    .container {
        max-width: 800px;
        margin: auto;
        background: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h2 {
        text-align: center;
        margin-bottom: 20px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }

    table th,
    table td {
        border: 1px solid #ccc;
        padding: 10px;
        text-align: left;
    }

    table th {
        background: #f8f9fa;
    }

    a {
        text-decoration: none;
        color: #000000;
        border: 2px red;
    }

    a:hover {
        text-decoration: underline;
    }

    button {
        padding: 10px 15px;
        border: none;
        background:rgb(0, 136, 255);
        color: #000000;
        border-radius: 5px;
        cursor: pointer;
        margin: 6px;
    }
</style>

<body>
    <div class="container">
        <button><a href="main.php">Add User</a></button>

        <form method="GET">
            <input type="text" name="search" placeholder="Enter User ID"   value="<?php echo htmlspecialchars($_GET['search'] ?? ''); ?>">
            <button type="submit">Go</button>
        </form>

        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Mobile</th>
                    <th>Password</th>
                    <th>Role</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php
                $searchQuery = mysqli_real_escape_string($conn, $_GET['search'] ?? '');

                $sql = "SELECT users.id, users.name, users.email, users.mobile, users.password, user_roles.role_name 
                        FROM users 
                        LEFT JOIN user_roles ON users.role_id = user_roles.id";

                if (!empty($searchQuery)) {
                    $sql .= " WHERE users.id = '$searchQuery'";
                }

                $result = mysqli_query($conn, $sql);


                while ($row = mysqli_fetch_assoc($result)) {
                    echo "<tr>
                            <td>{$row['id']}</td>
                            <td>{$row['name']}</td>
                            <td>{$row['email']}</td>
                            <td>{$row['mobile']}</td>
                            <td>{$row['password']}</td>
                            <td>{$row['role_name']}</td>
                            <td>
                                <a href='update.php?id={$row['id']}'>Update</a> 
                                <a href='delete.php?id={$row['id']}'>Delete</a>
                            </td>
                        </tr>";
                }

                ?>
            </tbody>
        </table>
    </div>
</body>

</html>