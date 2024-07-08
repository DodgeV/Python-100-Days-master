'''
第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。
'''
# 不想搞web，跳过本题

from flask import Flask, request, jsonify, render_template  

app = Flask(__name__)  

todos = []  # 使用列表来存储待办事项  

@app.route('/')  
def index():  
    """显示待办事项列表的HTML页面"""  
    return render_template('index.html', todos=todos)  

@app.route('/api/todos', methods=['GET', 'POST'])  
def todos_api():  
    """处理待办事项的API"""  
    if request.method == 'POST':  
        data = request.json  
        new_todo = data.get('content')  
        if new_todo:  
            todos.append({'id': len(todos) + 1, 'content': new_todo, 'done': False})  
            return jsonify({'message': 'Todo added successfully'}), 201  
        else:  
            return jsonify({'error': 'Todo content cannot be empty'}), 400  
    elif request.method == 'GET':  
        return jsonify(todos)  

if __name__ == '__main__':  
    app.run(debug=True)

"""
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>TodoList</title>  
</head>  
<body>  
    <h1>TodoList</h1>  
    <ul>  
        {% for todo in todos %}  
            <li>{{ todo.content }} - {{ 'Done' if todo.done else 'Not Done' }}</li>  
        {% endfor %}  
    </ul>  

    <form action="/api/todos" method="post">  
        <input type="text" name="content" placeholder="Add new todo...">  
        <button type="submit">Add Todo</button>  
    </form>  

    <script>  
        document.querySelector('form').addEventListener('submit', function(event) {  
            event.preventDefault();  
            const content = document.querySelector('input[name="content"]').value;  
            fetch('/api/todos', {  
                method: 'POST',  
                headers: {  
                    'Content-Type': 'application/json',  
                },  
                body: JSON.stringify({ content }),  
            })  
            .then(response => response.json())  
            .then(data => {  
                const list = document.querySelector('ul');  
                const item = document.createElement('li');  
                item.textContent = `${data.content} - Not Done`;  
                list.appendChild(item);  
            })  
            .catch(error => console.error('Error:', error));  
        });  
    </script>  
</body>  
</html>
"""
