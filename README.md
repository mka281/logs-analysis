# Logs Analysis

This project is for Udacity's [[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About this project

### Task
"Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database."

### Questions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Database
The database includes three tables:

* The authors table includes information about the authors of articles.
* The articles table includes the articles themselves.
* The log table includes one entry for each time a user has accessed the site.


## How to run the code
1. Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
2. [Download](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) the VM configuration or clone [this repository](https://github.com/udacity/fullstack-nanodegree-vm)
3. `cd` inside that directory from your terminal. Then change directory to vagrant with `cd vagrant`
4. Start the Ubuntu Linux installation with `vagrant up`
5. When `vagrant up` is finished running, run `vagrant ssh` to log in to newly installed Linux VM
6. Run `cd /vagrant`
7. [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) the database, unzip and put it inside vagrant folder.
8. Load the data with `psql -d news -f newsdata.sql`
9. Clone this project with `git clone https://github.com/mka281/logs-analysis.git`
10. Run `cd logs-analysis`
11. Run the app with `python3 logs.py`