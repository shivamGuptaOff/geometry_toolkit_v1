class Coordinate:

    #   ----------- EXTRACT THE COFFICIENT OF LINE AS STANDARED FORM------------

    @staticmethod
    def extracting_the_cofficient_from_equation_of_line(line:"aX+bY+c=0")-> tuple:
        '''Takes line as format of ax+by+c=0'''
        final_line=Coordinate.standardize_line_equation(line)
        final_line=final_line.replace(" ","").replace("=0","")#replace spaces " " to ""
        Coordinate.correct_maths_operations(final_line)
        final_line=final_line.replace("x","@").replace("y","@")#replace x -> @ and y ->@
        coff=final_line.split("@")
        a,b,c=coff # coff=["a","b","c"]
        return (float(a),float(b),float(c)) 
    
    def __init__(self,x: "abscissa",y: "ordinate"):
        self.x=x
        self.y=y

    def __str__(self)-> str:
        return f'({self.x},{self.y})'# (x,y)

    #   ---------- METHOD RELATED TO ONE POINT ------------
    
    def calculation_for_single_point(self:"Coordinate")-> str:
        '''Return point of reflection of point {self} over x-Axis,y-Axis and about origin'''
        return f'Point of reflection of point {self} over X-Axis is: {self.reflect_over_x_axis}\nPoint of reflection of point {self} over Y-Axis is: {self.reflect_over_y_axis}\nPoint of reflection of point {self} about origin is: {self.reflect_about_origin}'

    #   ---------- METHOD RELATED TO TWO POINT ------------

    def calculation_for_two_points(self:"Coordinate",other:"Coordinate")->str:
        '''Return many type of operation using two points: distance,midpoint,slope,equation and slope of perpendicular line '''
        return f'Distance between point {self} and {other} is: {self.distance_between_two_point(other)}\nMidpoint of point {self} and {other} is: {self.midpoint_of_two_points(other)}\nSlope of line joining point {self} and {other} is: {self.slope_of_line_joining_two_point(other)}\nEquation of line joining point {self} and {other} is: {self.equation_of_line_joining_two_point(other)}\nSlope of line which is perpendicular to line joining point {self} and {other} is: {self.slope_of_line_perpenicular_to_line_joining_two_points(other)}'
    
    #   ---------- METHOD RELATED TO THREE POINT ------------

    def calculation_for_three_points(self,other1:"Coordinate",other2:"Coordinate")-> str:
        '''Return many type of operation using three points: area,perimeter,type of triangle formed,coordinare of diff type of centre and about collinearity '''
        return f'Area of triangle formed by point {self},{other1} and {other2} is: {self.area_of_triangle_formed_by_given_three_points(other1,other2)}\nType of triangle formed by given point {self},{other1} and {other2} is: {self.type_of_triangle_formed_by_given_three_points(other1,other2)}\nPerimeter of triangle formed by point {self},{other1} and {other2} is: {self.perimeter_of_triangle_formed_by_given_three_points(other1,other2)}\nIs right-angle triangle formed by point {self},{other1} and {other2} is: {self.is_right_angle_trangle_formed_by_given_three_points(other1,other2)}\n{self.coordinate_of_different_types_of_centre_in_triangle(other1,other2)}\nIs given point {self},{other1} and {other2} are colinear: {self.is_colinear_given_three_points(other1,other2)}\n{self.coordinate_of_different_types_of_centre_in_triangle(other1,other2)}'

    #   ---------- METHOD RELATED TO TRIANGLE ------------
  
    def coordinate_of_different_types_of_centre_in_triangle(self,other1:"Coordinate",other2:"Coordinate")-> str:
        '''Return coordinate of diff type of centre formed in triangle'''
        return f'Coordinate of centroid of triangle is: {self.centroid_of_traingle_formed_by_given_three_points(other1,other2)}\nCoordinate of incentre of triangle is: {self.incentre_of_triangle_formed_by_given_three_points(other1,other2)}\nCoordinate of circumcentre of triangle is: {self.circumcentre_of_triangle_given_three_points(other1,other2)}\nCoordinate of orthocentre of triangle is: {self.orthocentre_of_triangle_given_three_points(other1,other2)}'  

    #   ---------- METHOD RELATED TO ONE POINT AND ONE LINE ------------
    
    def calculation_for_line_and_point(self:"Coordinate",line:"aX+bY+c=0")-> str:
        '''It returns distance between point and line,is point lies on line,image and foot of perpendicular about line taking point and line'''
        return f'Distance between point {self} and line {line} is: {self.distance_between_given_point_and_line(line)}\nIs point {self} lies on line {line} is: {self.is_point_lies_on_line(line)}\nCoordinate of image of point {self} in line {line} is: {self.image_of_point_in_given_line(line)}\nCoordinate of foot of perpendicular of point {self} in line {line} is: {self.foot_of_perpendicular_of_point_in_given_line(line)}'

    #   ---------- METHOD RELATED TO ONE LINE ------------

    @staticmethod
    def calculation_for_single_line(line:"aX+bY+c=0")->str:
        '''It takes line as parameter and return standered form of line,coff of (x,y,constant) and slope of thid line'''
        return f'Equation of standardize form of line {line} is: {Coordinate.standardize_line_equation(line)}\nCofficients of standardize form of line {line} is: {Coordinate.extracting_the_cofficient_from_equation_of_line(line)}\nSlope of given line {line} is: {Coordinate.extracting_slope_from_line(line)}'
    
    #   ---------- METHOD RELATED TO TWO LINE ------------

    @staticmethod
    def calculation_for_two_line(line1:"aX+bY+c=0",line2:"aX+bY+c=0")->str:
        '''return point of intersection of two lines'''
        intersection_point=Coordinate.point_of_intersection_of_two_line(line1,line2)
        return f'{Coordinate.relation_between_two_lines(line1,line2)}\nPoint of intersection of {line1} and {line2} is: {intersection_point}'
    
    #   ---------- METHOD RELATED TO TWO POINT AND RATIO------------

    def calculation_for_intersection_for_two_point(self,other:"Coordinate",ratio:"a:b")->str:
        '''return point of internal and external division using ratio'''
        return f'Internal division point of point {self} and {other} using ratio {ratio} is: {self.internal_division_of_line_joining_two_points(other,ratio)}\nExternal division point of point {self} and {other} using ratio {ratio} is: {self.external_division_of_line_joining_two_points(other,ratio)} '

    #   ---------- METHOD RELATED TO POINT AND SLOPE ------------
    
    def equation_of_line_given_point_and_slope(self,m:"a")-> str:
        '''return equation of line taking point and slope as parameter'''
        if m=='Undefined': 
            if self.x <0:
                return f'1X-0Y +{abs(self.x)}= 0'#check if line is parallel to Y axis
            return f'1X-0Y -{self.x}= 0' # eq of line parallel to y axis is X= constant
        elif float(m)==0.0:
            if self.y <0:
                return f'0X+1Y+{abs(self.y)}=0' #check if line is parallel to Y axis
            return f'0X+1Y-{self.y}=0' # eq of line parallel to y axis is X= constant
        else:
            
            c=round((float(m)*(self.x)-self.y),2)
            if c<0:
                return f'{float(m)}X-1Y +{abs(c)}=0'
            return f'{float(m)}X-1Y -{c}=0'

    #   ---------- METHOD RELATED TO RELATION BETWEEN TWO LINE ------------

    @staticmethod 
    def relation_between_two_lines(line1:"aX+bY+c=0",line2:"aX+bY+c=0")->str:
        '''return nature of two lines '''
        if (Coordinate.is_parallel_lines(line1,line2)==True):
            return f'line {line1} and {line2} are Parallel to each other'
        elif(Coordinate.is_intersecting_lines(line1,line2)==True):
            if (Coordinate.is_perpendicular_lines(line1,line2)==True):
                return f'line {line1} and {line2} are Perpendicular to each other'
            return f'line {line1} and {line2} are Intersecting'

    #   ----------- DISTANCE BETWEEN TWO POINT ------------
    
    def distance_between_two_point(self,other:"Coordinate")-> float:
        # distance=((x1-x2)**2 +(y1-y2)**2)**(1/2)
        d=round(((self.x-other.x)**2+(self.y-other.y)**2)**(1/2),2) # Round the disrance to two decimal places
        return d

    #   ----------- MID-POINT OF TWO POINT ------------

    def midpoint_of_two_points(self,other:"Coordinate")-> "Coordinate":
        #(((x1+x2)/2),((y1+y2)/2))
        return Coordinate(((self.x+other.x)/2),((self.y+other.y)/2))

    #   ----------- SLPOE OF LINE JOINING TWO POINT ------------


    def slope_of_line_joining_two_point(self,other:"Coordinate")-> float or str or int:
        #slope=(y2-y1)/(x2-x1)
        if (other.x-self.x)==0: #Check if line is parallel to Y axis
            return 'Undefined'
        if (other.y-self.y)==0:
            return 0 #Check if line is parallel to X axis
        m= round((other.y-self.y)/(other.x-self.x),2)
        return m

    #   ----------- EQUATION OF LINE JOINING TWO POINT ------------

    def equation_of_line_joining_two_point(self,other:"Coordinate")-> str:
        # eq-> y-y1=slope(x-x1).After rearranging: slope*x -y = slope*x1 - y1
        m=self.slope_of_line_joining_two_point(other) # call slope method
        if m=='Undefined':
            if self.x <0:
                return f'1X-0Y +{abs(self.x)}= 0' #Check if line is parallel to Y axis
            return f'1X-0Y -{self.x}= 0' # Equation of line parallel to y axis is X= constant
        elif m==0:
            if self.y <0:
                return f'0X+1Y+{abs(self.y)}=0' #Check if line is parallel to Y axis
            return f'0X+1Y-{self.y}=0' # Equation of line parallel to y axis is X= constant
        else:
            c=round((m*(self.x)-self.y),2)
            if c<0:
                return f'{m}X-1Y + {abs(c)}=0'
            return f'{m}X-1Y - {c}=0'

    #   ----------- AREA OF TRIANGLE FORMED BY THREE POINTS ------------

    def area_of_triangle_formed_by_given_three_points(self,other1:"Coordinate",other2:"Coordinate")-> str:
        # Using determinant method to calculate area
        area=round(abs(1/2*((self.x*other1.y)-(self.x*other2.y)-(self.y*other1.x)+(self.y*other2.x)+(other1.x*other2.y)-(other2.x*other1.y))),2)
        if area==0:# If area is 0, points are colinear
            return f'Area of triangle is 0 which shows that given points are colinear'
        return f'Area of triangle formed by points {self} , {other1} and {other2} is : {area}'

    #   ----------- WHICH TYPE OF TRIANGLE FORMED BY THREE POINTS ------------

    def type_of_triangle_formed_by_given_three_points(self,other1:"Coordinate",other2:"Coordinate") -> str:
        d1=self.distance_between_two_point(other1) # call distance method
        d2=self.distance_between_two_point(other2)
        d3=other1.distance_between_two_point(other2)
        if (d1==d2) and (d1==d3): # Check if all three side lengths are same
            return f'Triangle formed by {self},{other1}and {other2} is : Equilateral'
        elif (d1==d2) or (d1==d3) or (d2==d3): # Check if  two side lengths are equal
            return f'Triangle formed by {self},{other1}and {other2} is : Isosceles'
        else:
            return f'Triangle formed by {self},{other1}and {other2} is : Scalene'

    #   ----------- PERIMETER OF TRIANGLE FORMED BY THREE POINTS ------------

    def perimeter_of_triangle_formed_by_given_three_points(self,other1:"Coordinate",other2:"Coordinate")-> float:
        d1=self.distance_between_two_point(other1)  # Call distance method
        d2=self.distance_between_two_point(other2)
        d3=other1.distance_between_two_point(other2)
        return round((d1+d2+d3),2)

    #   ----------- CHECK TRIANGLE FORMED BY THREE POINTS IS RIGHT-ANGLED OR NOT ------------

    def is_right_angle_trangle_formed_by_given_three_points(self,other1:"Coordinate",other2:"Coordinate")-> str:
        '''return formed ftiangle using three points are right-angled or not'''
        m1=self.slope_of_line_joining_two_point(other1)# Call slope method
        m2=self.slope_of_line_joining_two_point(other2)
        m3=other1.slope_of_line_joining_two_point(other2)
        
        if m1=='Undefined':

            if m2=='Undefined' or m3=='Undefined': # if more than two slope are undefined, the points are colinear 
                return "NO"
            elif m2==0 or m3==0:
                return "YES" # m1 indicates the line is vertical, and the other is horizontal (i.e., right-angled) 
            elif  ((m2*m3)==-1.0):
                return "YES"
            return "NO"

        elif m2=='Undefined':
            if m3=='Undefined':
                return "NO"
            elif m1==0 or m3==0:
                return "YES"
            elif  ((m1*m3)==-1.0):
                return "YES"
            return "NO"
        
        elif m3=='Undefined':
            
            if  ((m1*m2)==-1.0):
                return "YES"
            return "NO"

        else:
            if (((m1*m2)==-1.0)) or ((m2*m3)==-1.0)or ((m1*m3)==-1.0): # This line execute if all three are not undefined
                return "YES"
            return "NO"

    #   ----------- COORDINATE OF CENTROID OF TRIANGLE FORMED BY THREE POINTS ------------

    def centroid_of_traingle_formed_by_given_three_points(self,other1:"Coordinate",other2:"Coordinate")-> "Coordinate":
        return Coordinate(round(((self.x + other1.x+ other2.x)/3),2),round(((self.y + other1.y+ other2.y)/3),2))

    #   ----------- COORDINATE OF INCENTRE OF TRIANGLE FORMED BY THREE POINTS ------------

    def incentre_of_triangle_formed_by_given_three_points(self,other1:"Coordinate",other2:"Coordinate")->"Coordinate":
        if self.is_colinear_given_three_points(other1,other2)==False:
            #I=((a*x1 + b*x2 + c*x3)/(a+b+c),(a*y1 + b*y2 + c*y3)/(a+b+c))
            d1=self.distance_between_two_point(other1) # call distance method 
            d2=self.distance_between_two_point(other2)
            d3=other1.distance_between_two_point(other2)
            tempX=round((self.x*d3 + other1.x*d2 + other2.x*d1)/(d1 + d2 + d3),2)
            tempY=round((self.y*d3 + other1.y*d2 + other2.y*d1)/(d1 + d2 + d3),2)
            return Coordinate(tempX,tempY)
        return "Given points are colinear so no triangle formed"

    #   ----------- COORDINATE OF CIRCUMCENTRE OF TRIANGLE FORMED BY THREE POINTS ------------
    
    def circumcentre_of_triangle_given_three_points(self,other1:"Coordinate",other2:"Coordinate")->"Coordinate":
        if self.is_colinear_given_three_points(other1,other2)==False:
            # Check triangle formed or not
            n1=self.slope_of_line_perpenicular_to_line_joining_two_points(other1)
            n2=self.slope_of_line_perpenicular_to_line_joining_two_points(other2)
            n3=other1.slope_of_line_perpenicular_to_line_joining_two_points(other2)
            mid1=self.midpoint_of_two_points(other1)# Call midpoint method
            mid2=self.midpoint_of_two_points(other2)
            mid3=other2.midpoint_of_two_points(other1)
            
            
            if n1!= "Undefined":
                b1=mid1.equation_of_line_given_point_and_slope(f'{n1}')
            if n2!= "Undefined":
                b2=mid2.equation_of_line_given_point_and_slope(f'{n2}')
            if n3!= "Undefined":
                b3=mid3.equation_of_line_given_point_and_slope(f'{n3}')
            if n1== "Undefined":
                b1=mid1.equation_of_line_given_point_and_slope(n1)
            if n2== "Undefined":
                b2=mid2.equation_of_line_given_point_and_slope(n2)
            if n3== "Undefined":
                b3=mid3.equation_of_line_given_point_and_slope(n3)
            
            return Coordinate.point_of_intersection_of_two_line(b1,b3)
        else:
            return "Given points are colinear so triangle not formed "

    #   ----------- COORDINATE OF ORTHOCENTRE OF TRIANGLE FORMED BY THREE POINTS ------------

    def orthocentre_of_triangle_given_three_points(self,other1:"Coordinate",other2:"Coordinate")->"Coordinate":
        if self.is_colinear_given_three_points(other1,other2)==False:
            n1=self.slope_of_line_perpenicular_to_line_joining_two_points(other1)
            n2=self.slope_of_line_perpenicular_to_line_joining_two_points(other2)
            n3=other1.slope_of_line_perpenicular_to_line_joining_two_points(other2)
            
            if n1!= "Undefined":
                a1=other2.equation_of_line_given_point_and_slope(f'{n1}')
            if n2!= "Undefined":
                a2=other1.equation_of_line_given_point_and_slope(f'{n2}')
            if n3!= "Undefined":
                a3=self.equation_of_line_given_point_and_slope(f'{n3}')
            if n1== "Undefined":
                a1=other2.equation_of_line_given_point_and_slope(n1)
            if n2== "Undefined":
                a2=other1.equation_of_line_given_point_and_slope(n2)
            if n3== "Undefined":
                a3=self.equation_of_line_given_point_and_slope(n3)
            return Coordinate.point_of_intersection_of_two_line(a1,a3)
        else:
            return "Given points are colinear so triangle not formed "

    
    #   ----------- CHECK COLINEARITY ------------

    def is_colinear_given_three_points(self,other1:"Coordinate",other2:"Coordinate")-> bool:
        area=self.area_of_triangle_formed_by_given_three_points(other1,other2)
        if area=='Area of triangle is 0 which shows that given points are colinear':
            return True
        return False

    #   ----------- METHOD GIVES POINT OF INTERNAL-DIVISION ------------


    def internal_division_of_line_joining_two_points(self,other:"Coordinate",ratio:"a:b")-> "Coordinate":
        #ratio.split(":")->["a","b"] where a and b are integer
        tempX=round((float(ratio.split(":")[0])*other.x + float(ratio.split(":")[1])*self.x)/(float(ratio.split(":")[0]) +float(ratio.split(":")[1]) ),2)
        tempY=round((float(ratio.split(":")[0])*other.y + float(ratio.split(":")[1])*self.y)/(float(ratio.split(":")[0]) +float(ratio.split(":")[1]) ),2)
        return Coordinate(tempX,tempY)

    #   ----------- METHOD GIVES POINT OF EXTERNAL-DIVISION ------------

    def external_division_of_line_joining_two_points(self,other:"Coordinate",ratio:"a:b")-> "Coordinate":
        #ratio.split(":")->["a","b"] where a and b are integer
        if (float(ratio.split(":")[0]) -float(ratio.split(":")[1]) )!=0.0:
            tempX=round((float(ratio.split(":")[0])*other.x - float(ratio.split(":")[1])*self.x)/(float(ratio.split(":")[0]) -float(ratio.split(":")[1]) ),2)
            tempY=round((float(ratio.split(":")[0])*other.y- float(ratio.split(":")[1])*self.y)/(float(ratio.split(":")[0]) -float(ratio.split(":")[1]) ),2)
            return Coordinate(tempX,tempY)
        else:
            "Not valid ratio"

    #   ----------- METHOD RELATED TO ONE POINT ------------
    
    def reflect_over_x_axis(self)-> "Coordinate":
        return Coordinate(self.x,-self.y)

    #   ----------- METHOD RELATED TO ONE POINT ------------
    
    def reflect_over_y_axis(self)->"Coordinate":
        return Coordinate(-self.x,self.y)
    
    #   ----------- METHOD RELATED TO ONE POINT ------------

    def reflect_about_origin(self)->"Coordinate":
        return Coordinate(-self.x,-self.y)

    #   ----------- DISTANCE BETWEEN POINT AND LINE ------------

    def distance_between_given_point_and_line(self,line:"aX+bY+c=0")-> float: 
        # d=(abs((ax1+by1+c))/((a**2 + b**2)**2)
        t=Coordinate.extracting_the_cofficient_from_equation_of_line(line)
        tempNum=round(abs((t[0]*self.x) + (t[1]*self.y) +t[2]),2)
        tempDen=round(((t[0])**2+(t[1])**2)**(1/2),2)
        return round(tempNum/tempDen,2)

    #   ----------- METHOD GIVES POINT OF INTERSECTION OF TWO LINE ------------

    @staticmethod
    def point_of_intersection_of_two_line(line1:"aX+bY+c=0",line2:"aX+bY+c=0")-> "Coordinate":
        t1=Coordinate.extracting_the_cofficient_from_equation_of_line(line1)# Gives touple, values are cofficients of line1-> (a,b,c)
        t2=Coordinate.extracting_the_cofficient_from_equation_of_line(line2)
        tempY=((t1[0]*t2[2])-(t2[0]*t1[2]))/((t2[0]*t1[1])-(t1[0]*t2[1]))
        tempX=((t1[1]*t2[2])-(t2[1]*t1[2]))/((t2[1]*t1[0])-(t1[1]*t2[0]))
        return Coordinate(round(tempX,2),round(tempY,2))

    #   ----------- CHECK POINT SETISFIES LINE OR NOT ------------
    
    def is_point_lies_on_line(self,line:"aX+bY+c=0")->bool:
        t=Coordinate.extracting_the_cofficient_from_equation_of_line(line)# Gives touple, values are cofficients of line1-> (a,b,c)
        if ((t[0]*self.x)+(t[1]*self.y)+t[2])==0.0:
            return True
        return False

    #   ----------- SLOPE OF LINE WHICH IS NORMAL TO FORMED LINE USING TWO POINT ------------

    def slope_of_line_perpenicular_to_line_joining_two_points(self,other:"Coordinate"):
        '''return slope of line which is nprmal to line formed using these points'''
        m1=self.slope_of_line_joining_two_point(other)
        if type(m1)== str:#It indicates, slope of line formed is "Undefined"
            n1=0# So slope of line which is perpendicular to formed line =0 

        if m1==0:
            n1="Undefined"

        if type(m1)!=str and m1!=0:
            n1=round((-1/m1),2)
        return n1


    #   ----------- COORDINATE OF POINT OF IMAGE ------------

    def image_of_point_in_given_line(self,line:"aX+bY+c=0")->"Coordinate":

        t=Coordinate.extracting_the_cofficient_from_equation_of_line(line)
        tempX=round((((2*-t[0])*(t[0]*self.x + t[1]*self.y + t[2]))/((t[0])**2 + (t[1])**2)) + (self.x),2)
        tempY=round((((2*-t[1])*(t[0]*self.x + t[1]*self.y + t[2]))/((t[0])**2 + (t[1])**2)) + (self.y),2)
        return Coordinate(tempX,tempY)

    #   ----------- COORDINATE OF FOOT OF PERPENDICULAR ------------

    def foot_of_perpendicular_of_point_in_given_line(self,line:"aX+bY+c=0")->"Coordinate":
        t=Coordinate.extracting_the_cofficient_from_equation_of_line(line)
        tempX=round((((-t[0])*(t[0]*self.x + t[1]*self.y + t[2]))/((t[0])**2 + (t[1])**2)) + (self.x),2)
        tempY=round((((-t[1])*(t[0]*self.x + t[1]*self.y + t[2]))/((t[0])**2 + (t[1])**2)) + (self.y),2)
        return Coordinate(tempX,tempY)

    #   ----------- RETURN SLOPE OF LINE TAKING LINE AS INPUT ------------

    @staticmethod
    def extracting_slope_from_line(line:"aX+bY+c=0"):
        t=Coordinate.extracting_the_cofficient_from_equation_of_line(line) # gives tuple, values are cofficient 
        if abs(t[0])==0.0:#Check cofficient of x=0
            return 0.0
        if abs(t[1])!=0.0:
            return round(((-t[0])/(t[1])),2)
        return "Undefined"

    #   ----------- CHECK IF TWO LINES ARE PARALLEL OR NOT ------------

    @staticmethod    
    def is_parallel_lines(line1:"aX+bY+c=0",line2:"aX+bY+c=0"):
        m1=Coordinate.extracting_slope_from_line(line1)
        m2=Coordinate.extracting_slope_from_line(line2)
        if m1==m2:# Condition of parallel, slopes are equal
            return True
        return False
    
    #   ----------- CHECK IF TWO LINES ARE PERPENDICULAR OR NOT ------------
    
    @staticmethod 
    def is_perpendicular_lines(line1:"aX+bY+c=0",line2:"aX+bY+c=0"):
        m1=Coordinate.extracting_slope_from_line(line1)
        m2=Coordinate.extracting_slope_from_line(line2)
        if type(m1)==float and type(m2)== float:
            if round(m1*m2,1)==-1.0:
                return True
            return False
        if m1=="Undefined" and m2==0.0:
            return True
        elif m2=="Undefined" and m1==0.0:
            return True
        else: 
            return False

    #   ----------- CHECK IF TWO LINES ARE INTERSECTING OR NOT ------------

    @staticmethod 
    def is_intersecting_lines(line1:"aX+bY+c=0",line2:"aX+bY+c=0"):
        if Coordinate.is_parallel_lines(line1,line2) ==False:
            return True
        return False

    #   ----------- RETURN STANDERED FORM OF EQUATION OF LINE BUT NOT ALWAYS ------------

    @staticmethod
    def standardize_line_equation(line)-> "aX+bY+c=0":
        '''Ye tab kaam karega jab vo ek valid line ki equation ho and constant term x and y ke beech me na aaye
        ye kuch case me correct format nhi dega,
        jab equation pahle se simplyfly na ho jaise ki (2x+3y=5x+3y+10) ya fir vo ek line ki valid equation hi na ho'''
        try:
            line=line.replace(" ","")
            line=line.replace("X","x").replace("Y","y")
            templ=line.split("=")
            
            
            if ("x" in templ[0] ) and ("y" in templ[0] ):# (ax+by=c),(ax+by=0),(ax+by+c=0) and covers if order (x,y)->(y,x) etc. format ke liye
                temp_line=Coordinate.__reversing_format_handling(line)
                return Coordinate.correct_maths_operations(temp_line)

            elif("x" in templ[1] ) and ("y" in templ[1] ):#(c=ax+by) and (c=by+ax)
                res_line=templ[1]+"="+templ[0]
                temp_line=Coordinate.__reversing_format_handling(res_line)
                return Coordinate.correct_maths_operations(temp_line)

            elif ((( "x" in templ[0]) and("y" in  templ[1])) or (("y" in templ[0]) and("x" in  templ[1]))) :# (ax=by+c),(ax+c=by),(by+c=ax), (by=ax+c) and (ax=by) format ke liye
                p,q=len(templ[0]),len(templ[1])
                if p<q:
                    if ("x" in templ[0]):# For (ax=by+c)
                        b=templ[1].split("y")[0]
                        c=templ[1].split("y")[1]
                        if b=="":b="1"
                        if c=="":c="0"
                        temp_line=templ[0]+"-"+b+"y"+"-"+c+"=0"
                        return Coordinate.correct_maths_operations(temp_line)
                    if ("y" in  templ[0]):# For (by=ax+c)
                        a=templ[1].split("x")[0]
                        c=templ[1].split("x")[1]
                        if a=="":a="1"
                        if c=="":c="+0"
                        if a=="-":a="-1"
                        temp_line=a+"X"+"-"+templ[0]+ c+"=0"
                        return Coordinate.correct_maths_operations(temp_line)
                                
                if p>q:
                    if ("x" in templ[0]):# For (ax+c=by)
                        a=templ[0].split("x")[0]
                        c=templ[0].split("x")[1]
                        if a=="":a="1"
                        if c=="":c="+0"
                        temp_line= a+"X"+"-"+templ[1]+ c+"=0"
                        return Coordinate.correct_maths_operations(temp_line)
                    if ("y" in  templ[0]):# For (by+c=ax)
                        b=templ[0].split("y")[0]
                        c=templ[0].split("y")[1]
                        if b=="":b="1"
                        if c=="":c="0"
                        temp_line=templ[1]+"-"+b+"y"+"-"+c+"=0"
                        return Coordinate.correct_maths_operations(temp_line)
                if p==q:
                    if ("x" in templ[0]):# For (ax=by)
                        temp_line=templ[0]+"-"+templ[1]+ "+0"+"=0"
                        return Coordinate.correct_maths_operations(temp_line)
                    if ("y" in  templ[0]):# For (by=ax)
                        temp_line=templ[1]+"-"+templ[0]+ "+0"+"=0"
                        return Coordinate.correct_maths_operations(temp_line)

                            
                    
            elif (("x" in templ[0]) and (templ[1]!="0")):# (ax=c) format ke liye
                temp_line= templ[0]+"+0y"+"-"+templ[1]+"=0"
                return Coordinate.correct_maths_operations(temp_line)

            elif ("y" in templ[0]) and (templ[1]!="0"): # (by=c) format ke liye
                temp_line="0x+"+templ[0]+"-"+templ[1]+"=0"
                return Coordinate.correct_maths_operations(temp_line)

            elif ("x" in templ[0]) and (templ[1]=="0"): # (x+c=0),(ax=0) format ke liye
                a=templ[0].split("x")[0]
                c=templ[0].split("x")[1]
                if a=="":a="1"
                if c=="":c="0"
                temp_line=a+"x"+"+0y"+"+"+c+"=0"
                return Coordinate.correct_maths_operations(temp_line)
            elif ("y" in templ[0]) and (templ[1]=="0"):# (by+c=0),(bx=0) format ke liye
                b=templ[0].split("y")[0]
                c=templ[0].split("y")[1]
                if b=="":b="1"
                if c=="":c="0"
                temp_line="0x"+"+"+b+"y"+"+"+c+"=0"
                return Coordinate.correct_maths_operations(temp_line)
        except:
            return "Kindly, give equation as format of (ax+by+c=0)"

    #   ----------- USING FOR CORRETION OF LINE ------------
         
    @staticmethod
    def correct_maths_operations(line):
        line=line.replace("--","+").replace("++","+")
        line=line.replace("-+","-").replace("+-","-")
        if "x" in line and line[0]!="x":
            x=line.index("x")
            if line[x-1]=="+" or line[x-1]=="-": line=line.replace("x","1x")
        if line[0]=="x":line=line.replace("x","1x")
        if "y" in line and line[0]!="y":
            y=line.index("y")
            if line[y-1]=="+" or line[y-1]=="-":line=line.replace("y","1y")
        if line[0]=="y": line=line.replace("y","1y")  
        if line[0]=="+":line=line[1:]
        return line
    
    #   ----------- IT HANDLES (Y,X) FORMAT OF LINE ------------

    def __reversing_format_handling(line):
        Coordinate.correct_maths_operations(line)
        line=line.replace(" ","")
        line=line.replace("X","x").replace("Y","y")
        templ=line.split("=")
        if templ[1]!="0" and(templ[0].index("x")<templ[0].index("y")):# (ax+by=c) format handling
            line=templ[0]+"-"+templ[1]+"=0"
            Coordinate.correct_maths_operations(line)
            return Coordinate.correct_maths_operations(line)
        elif templ[1]=="0" and(templ[0].index("x")<templ[0].index("y")): # (ax+by+c=0) and (ax+by=0)
            if templ[0][-1]=="y": # (ax+by=0) format ke liye
                return templ[0]+"+0"+"=0"
            return line # (ax+by+c=0) iske liye
        elif templ[1]!="0" and(templ[0].index("x")>templ[0].index("y")):# (by+ax=c) format ke liye
            ax=templ[0].split("y")[1]
            b=templ[0].split("y")[0]
            if b=="":b="1" # Check for  (y+ax=c)
            line=ax+"+"+b+"y"+"-"+templ[1]+"=0"
            return Coordinate.correct_maths_operations(line)  
        elif templ[1]=="0" and(templ[0].index("x")>templ[0].index("y")):#(by+ax+c=0) and (by+ax=0)
            
            if templ[0][-1]=="x":#(by+ax=0)
                ax=templ[0].split("y")[1]
                b=templ[0].split("y")[0]
                if b=="":b="1" # Check for (y+ax=0)
                line=ax+"+"+b+"y"+"+0"+"=0"
                return Coordinate.correct_maths_operations(line)

            else:#(by+ax+c=0)
                b=templ[0].split("y")[0]
                ax_c=templ[0].split("y")[1]
                a=ax_c.split("x")[0]
                c=ax_c.split("x")[1]
                if b=="":b="1"
                if c=="":c="1"
                if a=="":a="1"
                line=a+"x"+"+"+b+"y+"+c+"=0"
                return Coordinate.correct_maths_operations(line)

