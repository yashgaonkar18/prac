<?php
include 'connect.php';

$id = $_GET['id'];
$sql = "DELETE FROM users WHERE id=$id";
$result = mysqli_query($conn, $sql);

if ($result) {
    header('location:display.php');
} else {
    die("Error deleting record: " . $conn->error);
}
?>
