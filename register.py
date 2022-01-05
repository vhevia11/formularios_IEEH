import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfFileWriter, PdfFileReader

def complete_form(df,hospital):
    
    if os.path.isdir('F-IEEH'):
        None
    else:
        os.mkdir('F-IEEH')

    for i in range((len(df))):
        packet = io.BytesIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(packet, pagesize=letter)

        #Nombre Establecimiento
        text = can.beginText(30, 872)
        text.setFont("Courier", 12)
        text.textLine(hospital)
        can.drawText(text)

        #Código Establecimineto
        text = can.beginText(253, 872)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][2]))
        can.drawText(text)

        #Número Admisión
        text = can.beginText(349, 872)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][0]))
        can.drawText(text)

        #Número Ficha
        text = can.beginText(456, 872)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][4]))
        can.drawText(text)

        #Número Egreso
        text = can.beginText(503, 904)
        text.setCharSpace(0.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][1]))
        can.drawText(text)

        #Primer Apellido
        text = can.beginText(49, 828)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][5]))
        can.drawText(text)

        #Primer Apellido
        text = can.beginText(216, 828)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][6]))
        can.drawText(text)

        #Nombre Paciente
        text = can.beginText(432, 828)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][7]))
        can.drawText(text)

        #Tipo_id
        text = can.beginText(114, 803)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][8]))
        can.drawText(text)

        #RUT
        text = can.beginText(57, 781)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][9]))
        can.drawText(text)

        #DV
        text = can.beginText(158, 781)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][10]))
        can.drawText(text)

        #Pasaporte
        text = can.beginText(57, 755)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][11]))
        can.drawText(text)

        #Sexo
        text = can.beginText(272, 802)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][12]))
        can.drawText(text)

        #Día Nac
        text = can.beginText(452, 800)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][13]))
        can.drawText(text)

        #Mes Nac
        text = can.beginText(490, 800)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][14]))
        can.drawText(text)

        #Año Nac
        text = can.beginText(525, 800)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][15]))
        can.drawText(text)

        #Pueblo Indigena
        text = can.beginText(355, 773)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][18]))
        can.drawText(text)

        #Edad
        text = can.beginText(81, 736)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][16]))
        can.drawText(text)

        #Unidad Edad
        text = can.beginText(170, 736)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][17]))
        can.drawText(text)

        #Nombre País
        text = can.beginText(475, 728)
        text.setCharSpace(0.5)
        text.setFont("Courier", 12)
        text.textLine('CHILE')
        can.drawText(text)

        #Categoria Ocupacional
        text = can.beginText(47, 680)
        text.setCharSpace(0.1)
        text.setFont("Courier", 8)
        text.textLine(str(df.iloc[i][22]))
        can.drawText(text)

        #Glosa
        text = can.beginText(160, 703)
        text.setCharSpace(0.1)
        text.setFont("Courier", 8)
        text.textLine(str(df.iloc[i][23]))
        can.drawText(text)

        #Nvl Instrucción
        text = can.beginText(374, 682)
        text.setCharSpace(0.1)
        text.setFont("Courier", 8)
        text.textLine(str(df.iloc[i][21]))
        can.drawText(text)

        #Vía
        text = can.beginText(98, 600)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][28]))
        can.drawText(text)

        #Domicilio
        text = can.beginText(120, 600)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][26]))
        can.drawText(text)

        #Número
        text = can.beginText(525, 600)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][27]))
        can.drawText(text)

        #Comuna
        text = can.beginText(355, 584)
        text.setCharSpace(0.5)
        text.setFont("Courier", 9)
        text.textLine(str(df.iloc[i][184]))
        can.drawText(text)

        #Previsión
        text = can.beginText(56, 545)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][30]))
        can.drawText(text)

        #Tramo
        text = can.beginText(238, 542)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][31]))
        can.drawText(text)

        #Modalidad
        text = can.beginText(343, 541)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][32]))
        can.drawText(text)

        #Leyes Provisionales
        text = can.beginText(377, 551)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][33]))
        can.drawText(text)

        #Leyes Provisionales
        text = can.beginText(568, 539)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][34]))
        can.drawText(text)

        #Procedencia
        text = can.beginText(227, 502)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][35]))
        can.drawText(text)

        #Nombre Procedencia
        text = can.beginText(253, 503)
        text.setCharSpace(0.5)
        text.setFont("Courier", 4.5)
        text.textLine(str(df.iloc[i][36]))
        can.drawText(text)

        #Nombre Procedencia
        text = can.beginText(253, 503)
        text.setCharSpace(0.5)
        text.setFont("Courier", 4.5)
        text.textLine(str(df.iloc[i][36]))
        can.drawText(text)

        #Nombre Procedencia
        text = can.beginText(514, 502)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][37]))
        can.drawText(text)

        #Hora Ingreso
        text = can.beginText(104, 454)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][38]))
        can.drawText(text)

        #Minutos Ingreso
        text = can.beginText(137, 454)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][39]))
        can.drawText(text)

        #Día Ingreso
        text = can.beginText(183, 454)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][40]))
        can.drawText(text)

        #Mes Ingreso
        text = can.beginText(217, 454)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][41]))
        can.drawText(text)

        #Año Ingreso
        text = can.beginText(251, 454)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][42]))
        can.drawText(text)

        #U.F.
        text = can.beginText(507, 454)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][43]))
        can.drawText(text)
        
        #S.C.
        text = can.beginText(549, 454)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][44]))
        can.drawText(text)

        #Día 1er Traslado
        text = can.beginText(183, 438)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][45]))
        can.drawText(text)

        #Mes 1er Traslado
        text = can.beginText(217, 438)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][46]))
        can.drawText(text)

        #Año 1er Traslado
        text = can.beginText(251, 438)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][47]))
        can.drawText(text)

        #U.F.1er Traslado
        text = can.beginText(507, 438)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][48]))
        can.drawText(text)
        
        #S.C. 1er Traslado
        text = can.beginText(549, 438)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][49]))
        can.drawText(text)
        
        #Día 2do Traslado
        text = can.beginText(183, 423)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][50]))
        can.drawText(text)

        #Mes 2do Traslado
        text = can.beginText(217, 423)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][51]))
        can.drawText(text)

        #Año 2do Traslado
        text = can.beginText(251, 423)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][52]))
        can.drawText(text)

        #U.F. 2do Traslado
        text = can.beginText(507, 423)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][53]))
        can.drawText(text)

        #S.C. 2do Traslado
        text = can.beginText(549, 423)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][54]))
        can.drawText(text)
        
        #Día 3er Traslado
        text = can.beginText(183, 408)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][55]))
        can.drawText(text)

        #Mes 3er Traslado
        text = can.beginText(217, 408)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][56]))
        can.drawText(text)

        #Año 3er Traslado
        text = can.beginText(251, 408)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][57]))
        can.drawText(text)

        #U.F. 3er Traslado
        text = can.beginText(507, 408)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][58]))
        can.drawText(text)

        #S.C. 3er Traslado
        text = can.beginText(549, 408)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][59]))
        can.drawText(text)
        
        #Día 4to Traslado
        text = can.beginText(183, 392)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][60]))
        can.drawText(text)

        #Mes 4to Traslado
        text = can.beginText(217, 392)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][61]))
        can.drawText(text)

        #Año 4to Traslado
        text = can.beginText(251, 392)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][62]))
        can.drawText(text)

        #U.F. 4to Traslado
        text = can.beginText(507, 392)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][63]))
        can.drawText(text)

        #S.C. 4to Traslado
        text = can.beginText(549, 392)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][64]))
        can.drawText(text)
        
        #Hora Egreso
        text = can.beginText(94, 353)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][90]))
        can.drawText(text)

        #Minutos Egreso
        text = can.beginText(127, 353)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][91]))
        can.drawText(text)

        #Día Egreso
        text = can.beginText(171, 353)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][92]))
        can.drawText(text)

        #Mes Egreso
        text = can.beginText(206, 353)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][93]))
        can.drawText(text)

        #Año Egreso
        text = can.beginText(240, 353)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][94]))
        can.drawText(text)

        #U.F. Egreso
        text = can.beginText(508, 357)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][95]))
        can.drawText(text)

        #S.C. Egreso
        text = can.beginText(549, 357)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][96]))
        can.drawText(text)
        
        #Días Estada
        text = can.beginText(105, 335)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][97]))
        can.drawText(text)

        #Condición al Alta
        text = can.beginText(252, 336)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][98]))
        can.drawText(text)

        #Destino al Alta
        text = can.beginText(283, 361)
        text.setCharSpace(4.5)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][99]))
        can.drawText(text)

        #Diagnóstico Principal
        text = can.beginText(138, 309)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][100]))
        can.drawText(text)

        #Diagnóstico Principal
        text = can.beginText(522, 309)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][101]))
        can.drawText(text)

        #Causa Externa
        text = can.beginText(138, 295)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][102]))
        can.drawText(text)

        #Causa Externa Código
        text = can.beginText(522, 295)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][103]))
        can.drawText(text)

        #Diagnóstico 2
        text = can.beginText(138, 282)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][104]))
        can.drawText(text)

        #Código Diag 2
        text = can.beginText(522, 282)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][105]))
        can.drawText(text)

        #Diagnóstico 3
        text = can.beginText(138, 268)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][106]))
        can.drawText(text)

        #Código Diag 3
        text = can.beginText(522, 268)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][107]))
        can.drawText(text)

        #Intervención Quirúrgica
        text = can.beginText(152, 172)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][122]))
        can.drawText(text)

        #Intervención Quirúrgica Nombre
        text = can.beginText(180, 161)
        text.setCharSpace(0.5)
        text.setFont("Courier", 9)
        text.textLine(str(df.iloc[i][123]))
        can.drawText(text)

        #Intervención Quirúrgica 2 Nombre
        text = can.beginText(180, 148)
        text.setCharSpace(0.5)
        text.setFont("Courier", 9)
        text.textLine(str(df.iloc[i][124]))
        can.drawText(text)

        #Procedimiento
        text = can.beginText(62, 107)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][126]))
        can.drawText(text)

        #Procedimiento 1 Nombre
        text = can.beginText(242, 121)
        text.setCharSpace(0.5)
        text.setFont("Courier", 9)
        text.textLine(str(df.iloc[i][127]))
        can.drawText(text)

        #Procedimiento 2 Nombre
        text = can.beginText(242, 106)
        text.setCharSpace(0.5)
        text.setFont("Courier", 9)
        text.textLine(str(df.iloc[i][128]))
        can.drawText(text)

        #Apellido Paterno Profesional
        text = can.beginText(30, 60)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][140]))
        can.drawText(text)

        #Apellido Materno Profesional
        text = can.beginText(145, 60)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][141]))
        can.drawText(text)

        #Nombre Profesional
        text = can.beginText(260, 60)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][142]))
        can.drawText(text)

        #RUN Profesional
        text = can.beginText(58, 35)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][143]))
        can.drawText(text)

        #DV Profesional
        text = can.beginText(160, 35)
        text.setCharSpace(4.4)
        text.setFont("Courier", 12)
        text.textLine(str(df.iloc[i][144]))
        can.drawText(text)

        #Especialidad Profesional
        text = can.beginText(335, 78)
        text.setCharSpace(0.5)
        text.setFont("Courier", 11)
        text.textLine(str(df.iloc[i][186]))
        can.drawText(text)

        #Datos recién nacido
        #Condición al nacer 1
        text = can.beginText(145, 215)
        text.setCharSpace(4.4)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][146]))
        can.drawText(text)

        #Sexo al nacer 1
        text = can.beginText(245, 215)
        text.setCharSpace(4.4)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][147]))
        can.drawText(text)

        #Peso al nacer 1
        text = can.beginText(330, 215)
        text.setCharSpace(24)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][148]))
        can.drawText(text)

        #Apgar al nacer 1
        text = can.beginText(455, 215)
        text.setCharSpace(0.5)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][149]))
        can.drawText(text)

        #Anomalia al nacer 1
        text = can.beginText(517, 215)
        text.setCharSpace(0.5)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][150]))
        can.drawText(text)

        #Condición al nacer 2
        text = can.beginText(145, 205.5)
        text.setCharSpace(4.4)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][151]))
        can.drawText(text)

        #Sexo al nacer 2
        text = can.beginText(245, 205.5)
        text.setCharSpace(4.4)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][152]))
        can.drawText(text)

        #Peso al nacer 2
        text = can.beginText(330, 205.5)
        text.setCharSpace(24)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][153]))
        can.drawText(text)

        #Apgar al nacer 2
        text = can.beginText(455, 205.5)
        text.setCharSpace(0.5)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][154]))
        can.drawText(text)

        #Anomalia al nacer 2
        text = can.beginText(517, 205.5)
        text.setCharSpace(0.5)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][155]))
        can.drawText(text)

        #Condición al nacer 3
        text = can.beginText(145, 196.7)
        text.setCharSpace(4.4)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][156]))
        can.drawText(text)

        #Sexo al nacer 3
        text = can.beginText(245, 196.7)
        text.setCharSpace(4.4)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][157]))
        can.drawText(text)

        #Peso al nacer 3
        text = can.beginText(330, 196.7)
        text.setCharSpace(24)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][158]))
        can.drawText(text)

        #Apgar al nacer 3
        text = can.beginText(455, 196.7)
        text.setCharSpace(0.5)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][159]))
        can.drawText(text)

        #Anomalia al nacer 3
        text = can.beginText(517, 196.7)
        text.setCharSpace(0.5)
        text.setFont("Courier", 10)
        text.textLine(str(df.iloc[i][160]))
        can.drawText(text)
        can.save()

        #move to the beginning of the StringIO buffer
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        # read your existing PDF
        existing_pdf = PdfFileReader(open("Formulario-IEEH-2019.pdf", "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open("F-IEEH/"+str(df.iloc[i][7])+" "+str(df.iloc[i][6])+" "+str(df.iloc[i][5])+".pdf", "wb")
        output.write(outputStream)
        outputStream.close()