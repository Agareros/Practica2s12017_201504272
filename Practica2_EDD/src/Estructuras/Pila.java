/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Estructuras;

import static Estructuras.Cola.webClient;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author TOSHIBA P55
 */
public class Pila {
    public void insertar(String num) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", num)
                .build();
        String r = getString("AgregarPila", formBody);
        System.out.println(r);

        String r2 = getString2("listarPila");
        System.out.println(r2);

    }

    public static String getString2(String metodo) {
        String retorno = "";
        try {
            URL url = new URL("http://127.0.0.1:5000/" + metodo);
            Request request = new Request.Builder().url(url).build();
            Response response = webClient.newCall(request).execute();
            retorno = response.body().string();
        } catch (IOException ex) {
            Logger.getLogger(Pila.class.getName()).log(Level.SEVERE, null, ex);
        }
        return retorno;
    }

    public static String getString(String metodo, RequestBody formBody) {
        try {
            URL url = new URL("http://127.0.0.1:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();
            return response_string;
        } catch (IOException ex) {
            Logger.getLogger(Pila.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
