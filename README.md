## My Simple Flask App with Docker


Okay, so here’s the journey of making my simple Flask app, putting it in Docker, and pushing it to GitHub.
Honestly, it was a rollercoaster. 😅

## What I Did

1. Made the Flask app

   * `app.py` has two routes: `/` and `/hello-world`.
   * Ran it locally with Python first to check if it works:

     ```
     python3 app.py
     ```
   * Works fine, showing `"You're home now!"` on `/`.

2. Installed Flask and requirements

   * Initially Python said: `ModuleNotFoundError: No module named 'flask'`
   * Fixed by running:

     ```
     pip3 install --user -r requirements.txt
     ```

3. Docker problems galore

   * Tried `docker run -p 5000:5000 simple-flask-app` but port 5000 was already used.
   * Learned to check with:

     ```
     lsof -i :5000
     kill -9 <PID>
     ```
   * Then I changed the port in Python to 5000 and ran Docker on host port 5001:

     ```
     docker run -p 5001:5000 simple-flask-app
     ```
   * Some times the container name was already in use → had to remove old containers:

     ```
     docker stop $(docker ps -aq)
     docker rm $(docker ps -aq)
     ```

4. Git/GitHub stuff

   * First tried to push, got: `remote: Repository not found.`
   * Realized I had to use the correct repo: `simple-web-app-docker`
   * Ran `git push -u origin main --force` after syncing with remote.

5. Final running app

   * Docker container is running:

     ```
     docker run -p 5001:5000 --name simple-flask-app-container simple-flask-app
     ```
   * Access it: [http://localhost:5001](http://localhost:5001)
   * It works! `"You're home now!"` shows up. 

## Lessons Learned

* Always check which ports are being used before running Docker.
* Container names can conflict, so either remove old ones or rename.
* If Git says remote has changes, pull or force push carefully.
* Docker + Flask = tricky at first, but once you get the ports and container names right, it works beautifully.

---


