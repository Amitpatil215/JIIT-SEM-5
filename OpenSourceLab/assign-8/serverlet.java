package com.demoApp;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class AddServelet extends HttpServlet{
	public void service(HttpServletRequest req, HttpServletResponse res) throws IOException { //only service method name is allowed
		int i=Integer.parseInt(req.getParameter("num1"));
		int j=Integer.parseInt(req.getParameter("num2"));
		
		int k= i +j;
//		System.out.println("result is " + k);
		
		PrintWriter out = res.getWriter(); 
		out.println("result is " + k);
		
	}
}
