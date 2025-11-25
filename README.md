# 📘備忘錄系統
使用者可新增、查看備忘錄，且具備權限機制，僅**已登入的使用者可查看自己的備忘錄**。同時亦有API可新增、查看備忘錄，API僅限已認證獲得token的人員使用。(目前<u>尚未限制</u>獲得token人員訪問備忘錄)

## 📖 Introduction
測試**當前Django實踐能力**，學習依**功能**再**開發**。
Features為ChatGPT生成內容，開發中除了基礎功能外，額外學習以下內容

📝 初次使用功能
* CBV templeate default name
* Middleware
* Signal
* AJAX
* DRF-token
* DRF-JWT
* Form error msg
* Log setting

## 🚀 Features
### 第一階段：建立「個人筆記應用」
1. 建立專案 `notebook_project`，App 名為 `notes`。
2. Model：
    - `Note`（欄位：`title`, `content`, `created_at`）
3. View：
    - 顯示所有筆記（ListView）
    - 新增筆記（CreateView）
    - 查看單一筆記內容（DetailView）
4. Template：
    - 使用 `base.html` 實作模板繼承。
    - 加入簡單的 Bootstrap 樣式。
5. URL：
    - 設計 RESTful URL，如 `/notes/`, `/notes/1/`, `/notes/new/`。

### 第二階段：擴充筆記系統
1. 加入「分類（Category）」模型，讓筆記可選擇分類。
2. 使用 `ModelForm` 建立筆記新增表單。
3. 在表單中加入自訂驗證：
    - 標題不可重複。
    - 內容字數需大於 10。
4. 前端顯示驗證錯誤訊息。

### 第三階段：加入登入機制
1. 新增註冊、登入、登出頁面。
2. 使用 `LoginRequiredMixin` 限制未登入者無法新增或查看筆記。
3. 每位使用者只能看到自己的筆記。

### 第四階段：擴充筆記系統
1. 使用 **Class-based View** 重構所有視圖。
2. 使用 `post_save` signal：當筆記新增時，記錄 Log。
3. 建立自訂 Middleware：
    - 每次請求時印出使用者資訊與 URL。
4. 在 **Admin 後台** 自訂顯示樣式與篩選器。

### 第五階段：建立筆記 REST API
1. 使用 `Django REST Framework` 建立以下 API：
    - `GET /api/notes/`：取得所有筆記
    - `POST /api/notes/`：新增筆記
    - `GET /api/notes/<id>/`：查看單筆筆記
2. 加入 **Token 驗證**。
3. 實作前端 AJAX 呼叫 API。

## 📂 Project Structure
```plaintext
.
├── README.md
├── requirements.txt
└── notebook_project
    ├── db.sqlite3
    ├── manage.py
    ├── notebook_project
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── api_v1
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── notes
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── migrations
    │   ├── models.py
    │   ├── signals.py
    │   ├── static
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── users
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── middleware.py
        ├── migrations
        ├── models.py
        ├── signals.py
        ├── templates
        ├── tests.py
        ├── urls.py
        └── views.py
```

## 🛠 Tech Stack
* 語言: Python
* 框架: Django
* 前端: Bootstrap 4
* DB:  SQLite

## 📦 Installation & Run
1️⃣ 下載專案
```
git clone https://github.com/asfm4001/notebook.git
```

2️⃣ 建立env & 安裝套件
1. 建立虛擬環境
   ```
   python3 venv -m .venv
   ```
2. 進入虛擬環境
   ```
   source .venv/bin/activate
   ```
3. 安裝套件
   ```
   pip install -r requirements.txt
   ```

3️⃣ 啟動專案
```
python manage.py runserver
```

🧪 測試帳號
* Admin: admin/admin
* Test : test2/password2

## ⚙️ 設定 Configurations
略

## 📸 Demo
註冊
![註冊](/doc/register.png)
登入
![登入](/doc/login.png)
表單驗證
![表單驗證](/doc/validation.png)
Middleware紀錄request IP
![Middleware紀錄request IP](/doc/middleware.png)
Log日誌
![Log日誌](/doc/logging.png)
Token驗證
![Token驗證](/doc/api_without_token.png)

## 🗺 API Documentation
| Method | Endpoint                  | Description            | Auth |
|--------|---------------------------|------------------------|------|
| POST   | `/api_v1/token/`            | 取得Token               | Yes  |
| POST   | `/api_v1/jwt_token/`        | 取得JWT                 | Yes  |
| POST   | `/api_v1/jwt_refresh/`      | 取得新access            | Yes  |
| GET    | `/api/v1/notes/`            | 取得所有備忘錄           | Yes  |
| POST   | `/api/v1/notes/`            | 建立新備忘錄             | Yes  |
| GET    | `/api/v1/notes/<int:pk>>/ ` | 取得指定備忘錄資料        | Yes  |

## 📚 參考資料 References
略