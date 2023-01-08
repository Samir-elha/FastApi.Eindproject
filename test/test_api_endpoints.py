import requests
import pytest

def test_root_endpoint():
	response = requests.get("http://localhost:8000/")
	assert response.status_code == 200
	assert response.text == "todooo"

def test_todo_list_endpoint():
	response = requests.get("http://localhost:8000/todo")
	assert response.status_code == 200
	assert isinstance(response.json(), list)

def test_todo_item_endpoint():
	response = requests.get("http://localhost:8000/todo/1")
	assert response.status_code == 200
	assert response.json() == {"id": 1, "task": "some task"}

def test_create_todo_endpoint():
	data = {"task": "new task"}
	response = requests.post("http://localhost:8000/todo", json=data)
	assert response.status_code == 201
	assert response.text == "created todo item with id 2"

def test_update_todo_endpoint():
	data = {"task": "updated task"}
	response = requests.put("http://localhost:8000/todo/1", json=data)
	assert response.status_code == 200
	assert response.json() == {"id": 1, "task": "updated task"}

def test_delete_todo_endpoint():
	response = requests.delete("http://localhost:8000/todo/1")
	assert response.status_code == 204
	assert response.text == ""