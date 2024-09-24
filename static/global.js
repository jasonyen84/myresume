// 回到頂部按鈕的功能
var backToTopButton = document.getElementById("backToTop");

window.onscroll = function () {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        backToTopButton.style.display = "flex";
    } else {
        backToTopButton.style.display = "none";
    }
};

backToTopButton.onclick = function (e) {
    e.preventDefault();
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
};

// 複製網址功能
var copyUrlButton = document.getElementById("copyUrl");

copyUrlButton.onclick = function (e) {
    e.preventDefault();
    navigator.clipboard.writeText(window.location.href).then(function () {
        alert("網址已複製到剪貼簿");
    }, function () {
        alert("複製失敗，請手動複製");
    });
};