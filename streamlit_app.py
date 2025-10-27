import streamlit as st
import requests
from datetime import datetime
import os 

API_BASE = os.getenv('API_BASE', "http://localhost:8000")

st.title("Blog Application")

# Create User
st.header("Create User")
username = st.text_input("Username")
if st.button("Create User"):
    response = requests.post(f"{API_BASE}/users/", json={"username": username})
    if response.status_code == 201:
        st.success(f"User created! ID: {response.json()['id']}, Created: {response.json()['created_at']}")
    else:
        st.error(f"Error: {response.text}")

# Create Post
st.header("Create Post")
title = st.text_input("Title")
content = st.text_area("Content")
user_id = st.number_input("User ID", min_value=1)
if st.button("Create Post"):
    response = requests.post(f"{API_BASE}/posts/", json={"title": title, "content": content, "user_id": user_id})
    if response.status_code == 201:
        st.success(f"Post created! ID: {response.json()['id']}, Created: {response.json()['created_at']}")
    else:
        st.error(f"Error: {response.text}")

# View User
st.header("View User")
user_id_view = st.number_input("User ID to View", min_value=1)
if st.button("View User"):
    response = requests.get(f"{API_BASE}/users/{user_id_view}")
    if response.status_code == 200:
        user = response.json()
        st.write(f"ID: {user['id']}")
        st.write(f"Username: {user['username']}")
        st.write(f"Created: {user['created_at']}")
        st.write(f"Updated: {user['updated_at']}")
    else:
        st.error(f"Error: {response.text}")

# View Post
st.header("View Post")
post_id_view = st.number_input("Post ID to View", min_value=1)
if st.button("View Post"):
    response = requests.get(f"{API_BASE}/posts/{post_id_view}")
    if response.status_code == 200:
        post = response.json()
        st.write(f"ID: {post['id']}")
        st.write(f"Title: {post['title']}")
        st.write(f"Content: {post['content']}")
        st.write(f"User ID: {post['user_id']}")
        # Fetch username for display
        user_response = requests.get(f"{API_BASE}/users/{post['user_id']}")
        if user_response.status_code == 200:
            st.write(f"Posted by: {user_response.json()['username']}")
        st.write(f"Created: {post['created_at']}")
        st.write(f"Updated: {post['updated_at']}")
    else:
        st.error(f"Error: {response.text}")

# Delete Post
st.header("Delete Post")
post_id_delete = st.number_input("Post ID to Delete", min_value=1)
if st.button("Delete Post"):
    response = requests.delete(f"{API_BASE}/posts/{post_id_delete}")
    if response.status_code == 204:
        st.success("Post deleted!")
    else:
        st.error(f"Error: {response.text}")