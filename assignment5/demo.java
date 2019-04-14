
package oblig2;

import java.util.ArrayList;
import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class Oblig2 {
	
	byte[] bitArr;
	int maxNum, kjerner, siste, cntPrimtall;
	final int [] bitMask = {1,2,4,8,16,32,64};
	final int [] bitMask2 = {255-1,255-2,255-4,255-8,255-16,255-32,255-64};
	ArrayList<Long> faks;
	int traaderFerdige = 0;
	
	int primes[];
	int primesIndeks;
	ArrayList<Long> tempFaktorer;
	long tempTall;
	boolean funnet;

	
	CyclicBarrier barrier1, barrier2;
	
	public Oblig2(int num){
		maxNum = num;
		kjerner = Runtime.getRuntime().availableProcessors();
		bitArr = new byte[(num/14)+1];
		
		setAllPrime();
		barrier1 = new CyclicBarrier(kjerner+1);
		barrier2 = new CyclicBarrier(kjerner-1);
		siste = 1; 
	}

	public static void main(String[] args) {
		/**if(args.length != 1){
			System.out.println("Feil antall argumenter.\nBruk:\njava Oblig2 <maxNum>");
			return;
		}**/
		int n = 100;
		Oblig2 t = new Oblig2(n);
		t.generatePrimesSek();
		t.genPrimesPara();
		t.factorize100Sek();
		t.factorize100Para();
		
	}
	
	
	
	void printPrimtall(){
		System.out.println("Primtall  <= " + maxNum + ":");
		for(int i = 0; i<maxNum; i++){
			if(isPrime(i)) System.out.print(i + " ");
		}
	}
	
	
	void setAllPrime() {
		for (int i = 0; i < bitArr.length; i++) {
			bitArr[i] = (byte)127;
		}
	}
	
	
	void crossOut(int i){
		
		if(!((i%2) == 0)){
			int byteNr = i/14;
			int bitNr = (i%14)/2;
			
			bitArr[byteNr] = (byte) (bitArr[byteNr] & bitMask2[bitNr]);

		}
	}
	
	
	boolean isPrime(int i){
		if(i>maxNum){
			return false;
		}
		if(i == 2){
			return true;
		}
		if(i%2 == 0){
			return false;
		}
		int byteNr = i/14;
		int bitNr = (i%14)/2;
		return ((bitArr[byteNr] & bitMask[bitNr]) == bitMask[bitNr]);
		
	}
	
	
	void generatePrimesSek(){
		
		long t0 = System.nanoTime();
		crossOut(1);
		
		for(int i = 3; i<Math.sqrt(maxNum); i+=2){
			if(isPrime(i)){
				for(int j = i*i; j<maxNum; j+=i){
					crossOut(j);
					
				}
				
			}
		}
		long t1 = System.nanoTime();
		double tid = (t1-t0)/1000000.0;
		System.out.println("Genererte primtall sekvensiellt: " + tid);
		
	}

	
	void genPrimesPara(){
		setAllPrime();
		long t0 = System.nanoTime();
		crossOut(1);
		
		for(int i = 0; i<kjerner; i++){

			new Thread(new genPrimtall(neste())).start();
		}
		try {
			barrier1.await();
		} catch (InterruptedException | BrokenBarrierException e) {
			e.printStackTrace();
		}
		long t1 = System.nanoTime();
		double tid = (t1-t0)/1000000.0;
		System.out.println("\nGenererte primtall parallelt: " + tid);
	}
	
	
	 int neste(){
		int temp = hentNestePrimtall(siste);
		siste = temp;
		return temp;
	}
	
		 
	ArrayList<Long> factorize(long l){
		ArrayList<Long> faktorer = new ArrayList<>();
		
		int i = 2;
		long tempFaktor = l;
		
		while(i < Math.sqrt(tempFaktor)){
			if(tempFaktor == 1){
				break;
			}
			if(i == -1){
				faktorer.add(tempFaktor);
				break;
			}
			if((tempFaktor % i) == 0){
				faktorer.add((long) i);
				tempFaktor /= i;
			}
			else {
				i = hentNestePrimtall(i);
			}
		}
		if(tempFaktor > 1){
			faktorer.add(tempFaktor);
		}
		
		return faktorer;
	}
	
		
	 int hentNestePrimtall(int i){
		int retur = i;
		if((retur%2) == 0){
			retur++;
		} 
		else {
			retur+=2;
		}
		if(retur == 1){
			return 2;
		}
		while(! isPrime(retur) && retur < maxNum ){
			retur+=2;
		}
		if(retur > maxNum){
			return -1;
		}
		return retur;
	}
	
		
	void factorize100Sek(){
		long t0 = System.nanoTime();
		System.out.println("Faktoriserer sekvensiellt 100 tall t < " + maxNum + "*" + maxNum);
		
		long n = maxNum;
		for(long l = n * n - 100; l < n * n; l++){
			ArrayList<Long> temp = factorize(l);
			if(l < n*n-95 || l > n*n-6){
				System.out.print("\n" + l + " = " );
				for(long k: temp){
					System.out.print(k + " ");
				}
			}
		}
		long t1 = System.nanoTime();
		double tid = (t1-t0)/1000000.0;
		System.out.println("\n\n100 Faktoriseringer sekvensiellt med utskrift beregnet paa: " + tid + "ms");
		System.out.println("Tid pr. faktorisering = " + tid/100 + "ms");
		
	}
	
	
	/*
	 * Metode som parallellt faktoriserer de siste 100 tallene < n * n.
	 * */	
	void factorize100Para(){
		long t0 = System.nanoTime();
		cntPrimtall = tellPrimtall();
		primes = new int[cntPrimtall];
		primes[0] = 2;
		int indeks = 1;
		for(int i = 3; i<maxNum; i+=2){
			if(isPrime(i)){
				primes[indeks++] = i;
			}
		}
		
		System.out.println("\nFaktoriserer parallelt 100 tall t < " + maxNum + "*" + maxNum);
		long n = maxNum;
		for(long k = n*n-100; k<n*n; k++){
			ArrayList<Long> temp = facPara(k);
			if(k < n*n-95 || k > n*n-6){
				System.out.print("\n" + k + " = " );
				for(long l: temp){
					System.out.print(l + " ");
				}
			}
		}
		
		long t1 = System.nanoTime();
		double tid = (t1-t0)/1000000.0;
		System.out.println("\n\nFaktoriseringer parallelt med utskrift beregnet paa: " + tid + "ms");
		System.out.println("Tid pr. faktorisering = " + tid/100 + "ms");
		
	}
	
	/*
	 * Metode for Parallell faktorisering av parameteren l, og returnerer en ArrayList med den faktorer.
	 * */	
	
	synchronized void leggTilFaktor(long l){
		tempFaktorer.add(l);
		long prod = 1;
		for(long lo: tempFaktorer){
			prod*=lo;
		}
		if(prod == tempTall){
			if(tempTall == 39999){
				System.out.println("39999 funnet");
			}
			funnet = true;
		}
		
	}
	
	ArrayList<Long> facPara(long l){
		ArrayList<Long> faktorisert = new ArrayList<>();
		ArrayList<ArrayList<Long>> doubleList = new ArrayList<>(kjerner);
		barrier1 = new CyclicBarrier(kjerner+1);
		barrier2 = new CyclicBarrier(kjerner+1);
		
		tempTall = l;
		funnet = false;
		tempFaktorer = new ArrayList<>();
		
		
		ArrayList<facRunner> traadListe = new ArrayList<>();
		
		if(cntPrimtall == 0){
			cntPrimtall = tellPrimtall();
		}
		int start, slutt;
		
		for(int i = 0; i<kjerner; i++){
			start = (cntPrimtall/kjerner)*i;
			
			if(i == kjerner-1){
				slutt = cntPrimtall-1;
			}
			else{
				slutt = (cntPrimtall/kjerner *(i+1) -1);
			}
			facRunner temp = new facRunner(l, start, slutt);
			traadListe.add(temp);
			new Thread(temp).start();
			
		}
		try {
			barrier1.await();
		} catch (InterruptedException | BrokenBarrierException e) {
			e.printStackTrace();
		}
		
		if(!funnet){
			long prod = 1;
			for(long faktor: tempFaktorer){
				prod*=faktor;
			}
			tempFaktorer.add(tempTall/prod);
		}
		
		return tempFaktorer;
	}
	/*
	 * Metode som teller antall primtall. Til bruk i den parallelle faktoriseringen.
	 * */	
	int tellPrimtall(){
		int i = 1;
		for(int j = 3; j<=maxNum; j+=2){
			if(isPrime(j)){
				i++;
			}
		}
		return i;
	}
	
	/*
	 * Klasse for parallell generering av primtall. 
	 * */
	
	private class genPrimtall implements Runnable{
		int start;
		
		genPrimtall(int start){
			this.start = start;
		}
		/*
		 * metode som krysser ut multipler av parameteren i
		 * */
		void kryssUtMultipler(int i){
			int startNummer = i*i;
			for(int j = startNummer; j < maxNum; j+=i){
				crossOut(j);
			}
			
		}
		/*
		 * Traadbasert metode som krysser ut multipler av primtall, og derette henter neste.
		 * */
		@Override
		public void run() {
			kryssUtMultipler(start);
			int temp = neste();
			while( temp < Math.sqrt(maxNum)){
				kryssUtMultipler(temp);
				temp = neste();
				
			}
			try {
				barrier1.await();
			} catch (InterruptedException e) {
				e.printStackTrace();
			} catch (BrokenBarrierException e) {
				e.printStackTrace();
			}
		}
		
	}

	/*
	 * Klasse for paralell faktorisering.
	 * */
	private class facRunner implements Runnable{
		long l;
		int start, slutt;
		
		
		facRunner(long l, int start, int slutt){
			this.start = start;
			this.slutt = slutt;
			this.l = l;
		}
		

		/*
		 * Metode som fyller sin ArrayList med faktorer av l.
		 * */
		void genFac(){
			int faktor = primes[start];
			long rest = l;
			
			
			
			for (int i = start; i<slutt && !funnet; ){
				if(rest % faktor == 0){
					leggTilFaktor(faktor);
					rest /= faktor;
					
				}
				else {
					faktor = primes[++i];
				}
			}
			
			
		}
		

		@Override
		public void run() {
			genFac();
			try {
				barrier1.await();
			} catch (InterruptedException | BrokenBarrierException e) {
				e.printStackTrace();
			}
		}
		
	}
	
	

}
