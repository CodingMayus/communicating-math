from manim import *




# class CreateCircle(Scene):
#         def construct(self):
#                 circle = Circle() #create a circle
#                 circle.set_fill(PINK,opacity=0.5) #set the color and transparency
#                 self.play(Create(circle)) #show the circle on screen



class SquareToCircle(Scene):
            def construct (self):
                circle = Circle()
                circle.set_fill(PINK, opacity=0.5)
                
                square = Square()
                square.rotate(PI/4)
#the self references the instance of the scene that is being played
#and overall self.play is used to animate/transition objects in the scene.
#self.play shall play in order but 
#if you pass multiple animations in self.play it will play asynchronously
                self.play(Create(square))
                self.play(Transform(square,circle))
                self.play(FadeOut(square))  

        

class SquareAndCircle(Scene):
        def construct(self):
                circle = Circle() #create a circle
                circle.set_fill(PINK, opacity=0.5)#set color and transparency

                square = Square() #create a square
                square.set_fill(BLUE, opacity = 0.5) #set the color and transparency
                
                square.next_to(circle,RIGHT, buff = 0.5) #set the position
                #next_to is for positioning the first element in reference with the second ( one that is mentioned ).
                self.play(Create(circle),Create(square))


class AnimatedSquareToCircle(Scene):
    def construct (self):
            circle = Circle() #create a Circle
            square = Square() #create a Square
        
            #The functions Create and Transform return animations that will render with self.play 
            # .animate returns an animation like the latter and former, but does it dynamically instead of doing it before rendering.
            self.play(Create(square)) #creates the square
            self.play(square.animate.rotate(PI/4)) #rotates square dynamically (procrasination )
            self.play(Transform(square,circle)) #transforms the square into a circle
            self.play(square.animate.set_fill(PINK,opacity=0.5)) #color the circle on screen dynamically

#.animate vs conventional animation methods provided by manim


#when using .animate, the animation takes the starting state and the ending state and mashes them into each other - instead of directly which makes the transition look smooth.
#To "interpolate" in the context of animation (and mathematics in general) means to smoothly transition between two known values or states by estimating intermediate values.

class DifferentRotations(Scene):
       def construct(self):
                left_square = Square(color=BLUE, fill_opacity=0.7).shift( 2* LEFT)    # returns a transformed object which in this case translated.  
                right_square = Square(color=GREEN, fill_opacity=0.7).shift(2*RIGHT)   # returns a transformed object which in this case translated.
#it appears functions usually have capitals
                self.play(left_square.animate.rotate(PI),Rotate(right_square, angle = PI),run_time = 2
                          )
                
                self.wait()



#Transform vs ReplacementTransform
#The difference is that for Transform(prop1, prop2), transform will animate and transition the points of prop1 into prop2.
# Replacetransform in contrast, directly transforms prop1 to prop2.  Observe.

class TwoTransforms(Scene):
        def transform(self):
                a = Circle()
                b = Square()
                c = Triangle()
                self.play(Transform(a,b))
                self.play(Transform(a,c))
                self.play(FadeOut(a))
# I am still referencing Mobject a, as it merely transformed into the other objects.


        def replacement_transform(self):
                a = Circle()
                b = Square()
                c = Triangle()
                self.play(ReplacementTransform(a,b))
                self.play(ReplacementTransform(b,c))
                self.play(FadeOut(c))

#I am now referencing Mobject c because a literally became b, and b literally became c.

        def construct(self):
         self.transform()
         self.wait(0.5) #wait() by default is 1 second/
         self.replacement_transform()
        
#Transform might look better if transforming into a list of different objects.
# to prevent having to reference the last Mobject transformed use a loop.
#     for t in [t1,t2]:
  ##          self.play(Transform(a,t))