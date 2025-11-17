// 取得token
async function getToken() {
    const response = await fetch('/api_v1/token/', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            username: 'test2',
            password: 'password2'
        })
    });

    const data = await response.json();
    console.log("取得 token:", data);
    return data.token;   // 確認你的 API 回傳名稱是否是 token
}

// 呼叫 note API
async function callNote1WithToken() {
    const token = await getToken();
    if (!token) {
        alert("Token 取得失敗！");
        return;
    }

    const response = await fetch('/api_v1/notes/1/', {
        method: "GET",
        headers: {
            'Authorization': 'Token ' + token
        }
    });

    const result = await response.json();
    console.log(result);

    // 更新頁面
    document.getElementById("msg").innerText = result.created_at || "無資料";
}

async function callNote1WithOutToken() {
    const response = await fetch('/api_v1/notes/1/', {
        method: "GET",
    });

    const result = await response.json();
    console.log(result);

    // 更新頁面
    document.getElementById("msg").innerText = result.created_at || "無資料";
}

// 綁定按鈕事件
document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("btn");
    if (btn) {
        btn.addEventListener("click", callNote1WithOutToken);
    }
});
