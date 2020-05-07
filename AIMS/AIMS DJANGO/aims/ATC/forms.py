from django import forms
from . models import AircraftTypeModel,NewLocationModel,NewwOperatorModel,NewAircraftModel,NewDepartureModel,NewArrivalModel

class AircraftTypeForm(forms.ModelForm):
    Type_Indentifier=forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={
    'name':"type"
    }))
    Long_Name=forms.CharField(required=True,max_length=50,widget=forms.TextInput(attrs={
    'name':"lname",
    }))
    Short_Name=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"sname",

    }))
    Seating_Capacity=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={
    'name':"seatc",
    }))
    Max_Weight=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
    'name':"mweight",
    }))
    Wing_Span=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"wspan",
    }))
    Gear_Span=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"gspan",
    }))
    helicopter=forms.BooleanField(required=False,initial=False,label='helicopter',widget=forms.CheckboxInput(attrs={
    'name':"helicopter",
    }))
    supersonic=forms.BooleanField(required=False,initial=False,label='supersonic',widget=forms.CheckboxInput(attrs={
    'name':"ss",
    }))
    Remarks=forms.CharField(max_length=150,required=False,widget=forms.Textarea(attrs={
    'name':"remarks",
    'rows':'2','cols':'50'
    }))

    class Meta:
        model=AircraftTypeModel
        fields = '__all__'



LT=(('National','National'),('International','International'),('Defense','Defense'))
D=(('Local','Local'),('State','State'))
RT=(('Plains','Plains'),("Hilly","Hilly"),('Island','Island'))
ST=(('Available','Available'),('Unavailable','Unavailable'))

class NewLocationForm(forms.ModelForm):
    Location_Name=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
    'name':"locname"
    }))
    Location_Code=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
    'name':"loccode"
    }))
    IATA_Code=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"iata"
    }))
    Location_type=forms.ChoiceField(choices=LT,required=False,widget=forms.Select(attrs={
    'name':"loctype",
    }))
    Airport_Type=forms.ChoiceField(choices=LT,required=True,
    widget=forms.Select(attrs={
    'name':"atype"
    }))
    Division=forms.ChoiceField(choices=D,required=False,widget=forms.Select(attrs={
    'name':"division"
    }))
    Region=forms.ChoiceField(choices=RT,required=True,widget=forms.Select(attrs={
    'name':"reg"}))
    Status=forms.ChoiceField(choices=ST,required=True,widget=forms.Select(attrs={
    'name':"status"}))
    TNLC_DISCOUNT=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"discount"
    }))
    ILS=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"ils",
    }))
    Uncontrolled=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"uncontrolled",
    }))
    PCM_Seg=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"pcm",
    }))
    Address=forms.CharField(max_length=150,required=False,widget=forms.Textarea(attrs={
    'name':"address",
    'rows':'2',
    'cols':'50'
    }))

    class Meta:
        model=NewLocationModel
        fields='__all__'


CAT=(('National','National'),('International','International'))
FF=(('YES','YES'),('NO','NO'))
Agc=(('1','1'),('2','2'),('3','3'))

class NewwOperatorForm(forms.ModelForm):
    Operator_Name=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
    'name':"opcname"
    }))
    Operator_Code=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
    'name':"opccode"
    }))
    Phone=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"phone"
    }))
    Email=forms.EmailField(required=False,widget=forms.EmailInput(attrs={
    'name':"email"
    }))
    Category=forms.ChoiceField(choices=CAT,required=True,widget=forms.Select(attrs={
    'name':"categ"
    }))
    Free_Facility=forms.ChoiceField(choices=FF,required=True,widget=forms.Select(attrs={
    'name':"ff"
    }))
    Operator_Type=forms.ChoiceField(choices=CAT,required=False,widget=forms.Select(attrs={
    'name':"ot"
    }))
    ROF=forms.ChoiceField(choices=FF,required=False,widget=forms.Select(attrs={
    'name':"roff"
    }))
    Security_Deposit=forms.IntegerField(required=False,widget=forms.NumberInput(attrs={
    'name':"sd"
    }))
    Credit_Facility=forms.ChoiceField(choices=FF,required=True,widget=forms.Select(attrs={
    'name':"credf"
    }))
    PAN_Number=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"pan"
    }))
    TAN_Number=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"tan"
    }))
    AGC=forms.ChoiceField(choices=Agc,required=True,widget=forms.Select(attrs={
    'name':"agc"
    }))
    Scheduled=forms.ChoiceField(choices=FF,required=True,widget=forms.Select(attrs={
    'name':"sched"
    }))
    Service_Tax_Reg_No=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"strn"
    }))
    Counter_Category=forms.ChoiceField(choices=Agc,required=False,widget=forms.Select(attrs={
    'name':"cc"
    }))
    No_of_Counter_Alloted=forms.IntegerField(required=False,widget=forms.NumberInput(attrs={
    'name':"noc"
    }))
    No_of_Own_Counter=forms.IntegerField(required=False,widget=forms.NumberInput(attrs={
    'name':"noc"
    }))
    Monthly_CC_Category=forms.ChoiceField(choices=Agc,required=False,widget=forms.Select(attrs={
    'name':"nooc"
    }))
    FAX_NO=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"fax"
    }))
    Contact_Person=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"cp"
    }))
    GSA_Details=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
    'name':"gsa"
    }))
    Use_of_AAI_XRAY=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"xray",
    }))
    Use_of_Common_Counter=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"cc",
    }))
    Use_of_AAI_Housing=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"house",
    }))
    Use_of_AAI_Parking=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"pcm",
    }))
    Aero_Bridge=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"ab",
    }))
    Include_PSF_in_charge_Bill=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"psm",
    }))
    Common_Charges_for_All_Aircrafts=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"csaa",
    }))
    Common_Billing_For_SN=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"cbsn",
    }))
    Applicable_for_PSF_Discount=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"psf",
    }))
    Applicable_for_UDF_Discount=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"udf",
    }))
    Use_Ambulift=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
    'name':"alift",
    }))
    Address=forms.CharField(max_length=150,required=True,widget=forms.Textarea(attrs={
    'name':"address",
    'rows':'2',
    'cols':'50'
    }))
    class Meta:
        model=NewwOperatorModel
        fields='__all__'

Air_type=(('Airbus A320','Airbus A320'),('Boeing 737-800','Boeing 737-800'),('Airbus A321','Airbus A321'),
    ('Boeing 777-300ER','Boeing 777-300ER'))
Reg_t=(('Local','Local'),('National','National'),('International','International'))


class NewAircraftForm(forms.ModelForm):
    Registration_Number=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"regnew"
        }))
    Max_Weight=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"maxw"
        }))
    Aircraft_Type=forms.ChoiceField(choices=Air_type,required=True,widget=forms.Select(attrs={
        'name':"airtype"
        }))
    Registration_Type=forms.ChoiceField(choices=Reg_t,required=True,widget=forms.Select(attrs={
        'name':"regtype"
        }))
    Operator_Code=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"regtype"
        }))

    Seating_capacity=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={
        'name':"scap"
        }))
    LCN=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
        'name':"lcn"
        }))
    Height=forms.DecimalField(required=False,widget=forms.NumberInput(attrs={
        'name':"height"
        }))
    Owner_Name=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
        'name':"on"
        }))
    Leased_From=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
        'name':"lf"
        }))
    Valid_From=forms.DateField(required=False,widget=forms.DateInput(attrs={
        'name':"vf"
        }))
    Valid_Till=forms.DateField(required=False,widget=forms.DateInput(attrs={
        'name':"vt"
        }))
    Reference_Number=forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={
        'name':"refno"
        }))
    Cargo=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"cargo"
        }))
    Supersonic=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"supersonic"
        }))
    File_Upload=forms.FileField(required=False,widget=forms.FileInput(attrs={
        'name':"upfile"
        }))
    Remarks=forms.CharField(max_length=150,required=False,widget=forms.Textarea(attrs={
        'name':"remarkss",
        'rows':'2',
        'cols':'50'
        }))
    class Meta:
        model=NewAircraftModel
        fields='__all__'

NOF=(('Buoyant flight','Buoyant flight'),('Aerodynamic flight','Aerodynamic flight'))
Sch_C=(('Passenger','Passenger'),('Cargo','Cargo'))
Sch_T=(('Long','Long'),('Short','Short'))

class NewDepartureForm(forms.ModelForm):
    Nature_Of_Flight=forms.ChoiceField(choices=NOF,required=True,widget=forms.Select(attrs={
        'name':"nof"
        }))
    Schedule_Category=forms.ChoiceField(choices=Sch_C,required=True,widget=forms.Select(attrs={
        'name':"sc"
        }))
    Schedule_Type=forms.ChoiceField(choices=Sch_T,required=True,widget=forms.Select(attrs={
        'name':"st"
        }))
    Aircraft_Type=forms.ChoiceField(choices=Air_type,required=True,widget=forms.Select(attrs={
        'name':"at"
        }))
    RCS_Flight=forms.ChoiceField(choices=FF,required=False,widget=forms.Select(attrs={
        'name':"rcs"
        }))
    Valid_From=forms.DateField(required=True,widget=forms.DateInput(attrs={
        'name':"vf"
        }))
    Valid_Till=forms.DateField(required=True,widget=forms.DateInput(attrs={
        'name':"vt"
        }))
    Flight_Number=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"fn"
        }))
    Operator_Code=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"opcode"
        }))
    Arrival_Location=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"al"
        }))
    Flight_Status=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"fs"
        }))
    Scheduled_Time=forms.TimeField(required=True,widget=forms.TimeInput(attrs={
        'name':"st"
        }))
    Route=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"al"
        }))
    Mon=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"mon"
        }))
    Tue=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"tue"
        }))
    Wed=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"wed"
        }))
    Thu=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"thu"
        }))
    Fri=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"fri"
        }))
    Sat=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"sat"
        }))
    Sun=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"sun"
        }))


    class Meta:
        model=NewDepartureModel
        fields='__all__'

class NewArrivalForm(forms.ModelForm):
    Nature_Of_Flight=forms.ChoiceField(choices=NOF,required=True,widget=forms.Select(attrs={
        'name':"nof"
        }))
    Schedule_Category=forms.ChoiceField(choices=Sch_C,required=True,widget=forms.Select(attrs={
        'name':"sc"
        }))
    Schedule_Type=forms.ChoiceField(choices=Sch_T,required=True,widget=forms.Select(attrs={
        'name':"st"
        }))
    Aircraft_Type=forms.ChoiceField(choices=Air_type,required=True,widget=forms.Select(attrs={
        'name':"at"
        }))
    RCS_Flight=forms.ChoiceField(choices=FF,required=False,widget=forms.Select(attrs={
        'name':"rcs"
        }))
    Valid_From=forms.DateField(required=True,widget=forms.DateInput(attrs={
        'name':"vf"
        }))
    Valid_Till=forms.DateField(required=True,widget=forms.DateInput(attrs={
        'name':"vt"
        }))
    Flight_Number=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"fn"
        }))
    Operator_Code=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"opcode"
        }))
    Departure_Location=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"al"
        }))
    Flight_Status=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"fs"
        }))
    Scheduled_Time=forms.TimeField(required=True,widget=forms.TimeInput(attrs={
        'name':"st"
        }))
    Route=forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={
        'name':"al"
        }))
    Mon=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"mon"
        }))
    Tue=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"tue"
        }))
    Wed=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"wed"
        }))
    Thu=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"thu"
        }))
    Fri=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"fri"
        }))
    Sat=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"sat"
        }))
    Sun=forms.BooleanField(required=False,initial=False,widget=forms.CheckboxInput(attrs={
        'name':"sun"
        }))


    class Meta:
        model=NewArrivalModel
        fields='__all__'