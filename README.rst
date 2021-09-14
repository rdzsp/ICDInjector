!CDinjector
============
!CDinjector is tool for Auto `BlindSQLinjection <https://www.owasp.org/index.php/Blind_SQL_Injection>`_ in python code made by `impulseControlDisorder <https://www.youtube.com/channel/UCVUVmL2V9yAzUlx5K8r6HKg?view_as=subscriber>`_. This tool used python 3.

Watch Tutorial On `Youtube <https://youtu.be/O_KN-qVAguc>`_.

Installation
-------------
No need to installation, just install python 3 and run the script.

PIP Requirements
----------------
This tool used originally pip from python, so, you don't need to install any pip. If you have an error in pip requirements you need to install this pip

  pip3 install sys
  
  pip3 install requests
  
  pip3 install argparse

How To Use
----------
This tool used python 3, so you have to install python 3 and run:

  $ python3 inject.py --url [Victim URL] --fq [Fixing Queries (seperated by commas)] --method [Method [P]OST/[G]ET] --keyofdata [KEY of POST-DATA (Only           if the method is [P]OST)] --valueofdata [VALUE of POST-DATA (Only if the method is [P]OST)] --cookies [USING COOKIES? (yes/no)] --keyofvalue [KEY of COOKIE's VALUE (Only when using Cookies)] --valueofkey [VALUE of COOKIE's VALUE (Only when using Cookies)] --truestring [The string is appears only when the condition is TRUE] --logicaloperator [AND | OR (`reference <https://dev.mysql.com/doc/refman/8.0/en/logical-operators.html>`_)]

Details:

  \--url [Victim URL]:

    URL Victim, if using get method, the url must have [injection-point]
  
    example:
    \--url "http://localhost/dvwa/vulnerabilities/sqli/?id=1[injection-point]&Submit=Submit#"
    
    This [injection point] function is to determine the location where you want to inject a query

  \--fq [Fixing Queries (seperated by commas]:

    Fixing Queries, if the fixing queries is (') and (-- -) you can input ("',-- -") using a commas to seperated the fixing queries
    , and etc. You have to use escape string.
    
  \--method [Method [P]OST/[G]ET]:
    
    HTTP Methods, just input 'p' for POST OR 'g' for GET, `Difference Between HTTP POST and HTTP GET <https://www.tutorialspoint.com/listtutorial/Difference-between-GET-and-POST-method-in-HTTP/3916>`_.
    
  \--keyofdata [KEY of DATA (Only if the method is [P]OST)]:
  
    Key of Data, this is only used if the Method is POST, if using GET METHOD, you're not necessary to input the --keyofdata.
    POST-DATA is `Dictionary <https://www.tutorialspoint.com/python/python_dictionary.htm>`_, Dictionary have KEY and VALUE.

  \--valueofdata [VALUE of DATA (Only if the method is [P]OST)]:
  
    Value of Key, this is only used if the Method is POST, if using GET METHOD, you're not necessary to input the --valueofdata.
    POST-DATA is `Dictionary <https://www.tutorialspoint.com/python/python_dictionary.htm>`_, Dictionary have KEY and VALUE.
    
  \--cookies [Using Cookies? (y)es/(n)o]:
  
    `Cookies <http://www.whatarecookies.com/>`_, if you're using cookies, input "yes"/"y", if not, input "no"/"n".
    
  \--keyofvalue [KEY of COOKIE's VALUE (Only when using Cookies)]:
  
    Key of Value, this is only used when you're using Cookies. Cookies is `Dictionary <https://www.tutorialspoint.com/python/python_dictionary.htm>`_, Dictionary have KEY and VALUE.
    
  \--valueofkey [VALUE of COOKIE's KEY (Only when using Cookies)]:
  
    Value of Key, this is only used when you're using Cookies. Cookies is `Dictionary <https://www.tutorialspoint.com/python/python_dictionary.htm>`_, Dictionary have KEY and VALUE.
    
  \--truestring [TRUE string]:
  
    The string is appears only when the condition is TRUE.
    
  \--logicaloperator [OR | AND]:
  
    `REFERENCE <https://dev.mysql.com/doc/refman/8.0/en/logical-operators.html>`_  
    
    
Watch Tutorial On `Youtube <https://youtu.be/O_KN-qVAguc>`_.
