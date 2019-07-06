In this repo, three scripts are present
# Description of scripts
##  POC.py
This scrips is the simplest form of example using super for dependency injection and "hijacking" of this dependency.

I wrote it after having seen the excellent video https://www.youtube.com/watch?v=EiOglTERPEo

We are going to have a base class Pizza which will derive from its dough supplier;
In a second step we will create an alternative supplier with bio dough (organic), in one line a class PizzaBio will
be created : it will be a Pizza but we actually changed the class pointed by super() and used in Pizza.order_pizza()

The parent of Pizza is not changed but super() does not point to the parent but to the next in the order of "Method
resolution order" that can be seen in help(Pizza)

https://rhettinger.wordpress.com/2011/05/26/super-considered-super/


## dependency_injection_inheritance.py
Applying the same approach and with POC with non overlapping method names. 


## dependency_injection_no_inheritance.py
Comparison with the same thing using the creation of actual instances of providers stored in attibutes of seld in the 
```__init__``` functions.

# Conclusion

This was very interesting to see the super() mechanism;

the dependency injection mechanism based on inheritance seem pertinent to provide static 
ressources (in particular, there does not seem to rely on instances of the classes).