A=print
B=range
N=abs
M=len
G=''
import operator as C
E={'a':.0837,'b':.0193,'i':.0883,'o':.0753,'e':.0868,'z':.0533,'n':.0569,'r':.0415,'w':.0411,'s':.0413,'t':.0385,'c':.0389,'y':.0403,'k':.0301,'d':.0335,'p':.0287,'m':.0281,'u':.0206,'j':.0228,'l':.0224,'ł':.0238,'g':.0146,'ę':.0113,'h':.0125,'ą':.0079,'ó':.0079,'ż':.0093,'ś':.0072,'ć':.006,'f':.0026,'ń':.0016,'q':.0014,'ź':.0008,'v':.0004,'x':.0002}
F={'a':.0849,'b':.0207,'c':.0453,'d':.0338,'e':.1116,'f':.0181,'g':.0247,'h':.03,'i':.0754,'j':.0019,'k':.011,'l':.0548,'m':.0301,'n':.0665,'o':.0716,'p':.0316,'q':.0019,'r':.0758,'s':.0573,'t':.0695,'u':.0363,'v':.01,'w':.0128,'x':.0029,'y':.0177,'z':.0027}
def L(table):
	A=table;A=dict(sorted(A.items(),key=C.itemgetter(1),reverse=True));B=G
	for D in A.keys():B+=D
	return B
Q=L(E)
R=L(F)
def O(x,y):
	C=0
	for D in B(M(x)):
		F=x[D];A=-1
		for E in B(M(y)):
			if y[E]==F:A=N(E-D);break
		if A==-1:return-1
		else:C+=A
	return C
def D(tekst):
	I=tekst;P=I;I=G
	for A in P:
		if A in E.keys()or A in F.keys():I+=A
	P=None;S=M(I);B={}
	for A in I.lower():
		if A in B.keys():B[A]+=1
		else:B[A]=1
	for A in B.keys():B[A]=B[A]/S
	J=0;H=0;K=L(B);T=G.join([A if A in K else G for A in Q]);U=G.join([A if A in K else G for A in R]);C=O(K,T);D=O(K,U)
	if C==-1 and D==-1:H+=1
	elif D<C and D!=-1 or C==-1:H+=1
	else:J+=1
	C=0;D=0
	for A in B.keys():C+=N(B[A]-E[A]if A in E.keys()else 999);D+=N(B[A]-F[A]if A in F.keys()else 999)
	if D<C:H+=1
	else:J+=1
	C=0;D=0
	for A in B.keys():C+=(B[A]-E[A])**2 if A in E else 999;D+=(B[A]-F[A])**2 if A in F else 999
	C**=1/2.;D**=1/2.
	if D<=C:H+=1
	else:J+=1
	return'angielski'if H>J else'polski',(J,H)
def H():A('Program zrobiony przez Paweł Paszkiet (MZ)');B=input('Napisz swoje zdanie: ');E=None;C,F=D(B);A(f"Język to {C}")
if __name__=='__main__':H()