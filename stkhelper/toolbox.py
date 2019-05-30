
import os
import datetime

class TLE_Manager:
    
    
    """
    
    Class containing only static methods for processing TLE files.
    
    """
    
    @staticmethod
    def ParseTLE(filename):
    
        """
        
        Parses a TLE file of the given file name.
        
        Parameters:
            filename (str): Name of the TLE file.
            
        """
    
        #Create array for return value
        outputArray = []
    
        #Open TLE file
        tle = open(filename,'r')
    
        #Saves first and second lines to variables
        firstLine = tle.readline()
        secondLine = tle.readline()
    
        #Adds line to output array
        outputArray.append(firstLine)
        outputArray.append(secondLine)
    
        #Close tle file
        tle.close()
    
        return outputArray

    @staticmethod
    def GenerateTLE(application, sscNumber):
    
        """
    
        TESTING REQUIRED

        Retrieves TLE file for a satellite with a given SSC Number

        Parameters:
            application (uiApplication): Application object that holds the scenario.
            sscNumber (str || int): SSC Number of the satellite to retrieve TLE file from.
    
        """
        
        sscNumber = str(sscNumber)
        application.root.ExecuteCommand("CreateTLEFile * AGIServer " +
                os.getcwd() + "\\" + sscNumber + ".tle" + 
                " SSCNumber " + sscNumber)
   
class Toolbox:

    @staticmethod
    def ComputeCenterTarget(coordList):
        
        """
        
        Computes the coordinates for the center of an area target.
        
        Parameters:
            parsedLine (str): Line parsed from target list csv.
            
        Returns:
            midPoint (list): List containing name and coordinates of the middle of the area target.
            
        """
        latSum = 0.0
        lonSum = 0.0
        for point in coordList:
            latSum = latSum + float(point[0])
            lonSum = lonSum + float(point[0])
        
        midLat = latSum/float(len(coordList))
        midLon = lonSum/float(len(coordList))
        
        return (midLat,midLon)
    
    """
    Compares if time1 is greater than time2. If it is, it returns true. If
    it is not, it returns false.
    
    Parameters:
        time1 (datetime): Object to test.
        time2 (datetime): Object to compare to time1.
        
    Returns:
        True if time1 is greater than time2. Otherwise, it returns false.
        
    """
    
    @staticmethod
    def CompareTime(time1,time2):
        time1Elems = [time1.year,
                     time1.month,
                     time1.day,
                     time1.hour,
                     time1.minute,
                     time1.second,
                     time1.microsecond]
        
        time2Elems = [time2.year,
                     time2.month,
                     time2.day,
                     time2.hour,
                     time2.minute,
                     time2.second,
                     time2.microsecond]
        
        for i in range(len(time1Elems)):
            if time1Elems[i] > time2Elems[i]:
                return True
            else:
                pass
            
        return False
        

    """
    
    Converts time from STK format to datetime objects.
    
    Parameters:
        time1 (str): The time string from STK.
        
    Returns:
        timeObj1 (datetime): The datetime objects.
        
    """
    
    @staticmethod    
    def ConvertTime(time1):
        monthDict = {"Jan": 1,
                     "Feb": 2,
                     "Mar": 3,
                     "Apr": 4,
                     "May": 5,
                     "Jun": 6,
                     "Jul": 7,
                     "Aug": 8,
                     "Sep": 9,
                     "Oct": 10,
                     "Nov": 11,
                     "Dec": 12}
        
        time1 = str(time1)
        
        splitTime1 = time1.split(' ')
        day1 = splitTime1[0]
        month1 = monthDict[splitTime1[1]]
        year1 = splitTime1[2]
        
        clockTime1 = splitTime1[3]
        
        splitClockTime1 = clockTime1.split(':')
        hours1 = splitClockTime1[0]
        minutes1 = splitClockTime1[1]
        seconds1 = splitClockTime1[2].split('.')[0]
        microseconds1 = splitClockTime1[2].split('.')[1]
        
        timeObj1 = datetime.datetime(
                int(year1),
                int(month1),
                int(day1),
                hour=int(hours1),
                minute=int(minutes1),
                second=int(seconds1),
                microsecond=int(microseconds1))
        
        return timeObj1
    
    @staticmethod
    def GetTimeDelta(timeArray):
        
        """
        
        Computes the time difference between to time instances from STK.
        
        Parameters:
            timeArray (list): A list containting two time instances from STK.
            Each instance is in format: 'DD MM YYYY HH:mm:SS.sss'
            
        Returns:
            deltat (float): Time elapsed in seconds between the two instants.
            
        """
        
        timeObj1 = Toolbox.ConvertTime(str(timeArray[0]))
        timeObj2 = Toolbox.ConvertTime(str(timeArray[1]))
        
        timeDiff = timeObj2 - timeObj1
        print(timeDiff.days,timeDiff.seconds, timeDiff.microseconds)
        deltat = float(timeDiff.days*86400.0) + \
        float(timeDiff.seconds) + \
        (0.001*float(timeDiff.microseconds))
                    
        return deltat
        
