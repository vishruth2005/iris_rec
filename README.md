                                                 REPORT

This is a report on the major errors faced when the tasks were completed and the solutions through which i overcame them.

The errors were:

1.The first major error i got was while i was building the Dockerfile for the task 1.It was coming as gem not found as the gem downloaded was sqlite3(1.6.9) but dependency listed in Gemfile.lock was incorrect and called sqlite3-1.6.9-x86_64-linux.I spoke to the poc and was informed that the gemfile was updated so then i cloned the project again to solve the prob.

2.The second error i faced was when i created the database.It mentioned that the image was mysql in database.yml but i was using postgresl so i changed that to mysql.

3.Next was installing bundle during the docker compose build.I had to add the commands 
RUN gem install bundler:2.4.7
RUN gem update --system 3.2.3
in Dockerfile to successfully install the bundle.

4.Next it showed that a few dependencies like nidejs yarn etc.I solved it by putting 
RUN apk add --no-cache mariadb-connector-c-dev
RUN apk add --no-cache build-base nodejs tzdata yarn
I also had to change the image i used to ruby:2.6.10-alpine as the above couldnt be done using the previous image.

5.Next i had to select the correct Password and username given in the Database.yml to give access to vedant user created.I had to also encode the password using enc.erb as the password contained @.

6.Next one of the major probems i faced was that webpacker could'nt find application.js.Iworked on it for a while and found that manifest wasnt being generated.So i talked tothe poc and learnt that it was problem with webpacker and had to delete webpacker from the gemfile.I deleted it from the gemfile and its other mentions like in like in application.html.erb etc.Then the application was finally deployed successfully and i could see a page with tasks and a table and n option called new task.By this i had competed the first two tasks.

7.The last major error i faced was finding the right code directory and data directory while wting backup.py for task8.This was completed by looking up various resources in internet like reddit,baeldung etc.

The rest of the tasks were competed without any major hiccups as doing the first two were the main difficulty.After that it was just changing docker compose,dokerfile and adding a few files to match the requirements.
The tasks are hyperlinked in the file called tasks.md.

Overall it was a brainstorming, and learning experience as i leart a lot of new things not just related to docker in these two weeks as i attempted these tasks.

                                                                                  -Vishruth
                                                                                   231DS034