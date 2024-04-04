import tkinter as tk
from tkinter import Button, ttk,messagebox
import random
import numpy as np

def I(qnum=None):
    
    matrix = np.array([[1,0],
                      [0,1]])

    if qnum == None:
        
        pass
        
    elif qnum == 2:
        
        matrix = np.kron(matrix,matrix)
    
    return matrix

def Z(qnum=None):
    
    matrix = np.array([[1,0],
                      [0,-1]])

    if qnum == None:
        
        pass
        
    elif qnum == 2:
        
        matrix = np.kron(matrix,I())
    
    return matrix

def Y(qnum=None):
    
    matrix = np.array([[0,-1j],
                      [1j,0]])

    if qnum == None:
        
        pass
        
    elif qnum == 2:
        
        matrix = np.kron(matrix,I())
    
    return matrix


def X(qnum=None):
    
    matrix = np.array([[0,1],
                      [1,0]])
    if qnum == None:
        
        pass
        
    elif qnum == 2:
        
        matrix = np.kron(matrix,I())
    
    return matrix

def H(qnum=None):
    
    matrix = np.array([[1,1],[1,-1]]/np.sqrt(2))
    
    if qnum == None:
        
        pass
    elif qnum == 2:
        
        matrix = np.kron(matrix,I())
        
    
    return matrix

def CZ():
    
    matrix = np.array([[1,0,0,0],
                       [0,1,0,0],
                       [0,0,1,0],
                       [0,0,0,-1]])
                       
    return matrix

def CNOT():
    
    matrix = np.array([[1,0,0,0],
                       [0,1,0,0],
                       [0,0,0,1],
                       [0,0,1,0]])
                       
    return matrix

def simil(arr1, arr2):

	# Similarity between two array in input

    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    
    dot_product = np.dot(arr1, arr2)
    
    magnitude_arr1 = np.linalg.norm(arr1)
    magnitude_arr2 = np.linalg.norm(arr2)
    
    similarity = dot_product / (magnitude_arr1 * magnitude_arr2)
    
    return similarity

def entangle(state1,state2):

	return np.kron(state1,state2)

def disentangle_check(state):

    if state[0]==0 and state[1]==0:
        return True

    elif state[0]==0 and state[2] == 0:
    	return True
    elif state[1]==0 and state[3] == 0:
    	return True

    elif state[2]==0 and state[3] == 0:
    	return True
    else:
        return False

def disentangle(state):
    for i in range(2):
        if state[i] * state[i + 2] < 0:
            sign = False  
        sign = True

    if state[0]==0 and state[1]==0 and sign:
        return  np.array([0., 1.]),np.array([1, 1]) / np.sqrt(2)
    elif state[0]==0 and state[1]==0 and not sign:
        return np.array([0., 1.]),np.array([1, -1]) / np.sqrt(2)

    elif state[0]==0 and state[2] == 0 and sign:
    	return  np.array([1, 1]) / np.sqrt(2),np.array([0., 1.])
    elif state[0]==0 and state[2] == 0 and not sign:
    	return  np.array([1, -1]) / np.sqrt(2),np.array([0., 1.])

    elif state[1]==0 and state[3] == 0 and sign:
    	return  np.array([1, 1]) / np.sqrt(2),np.array([0., 1.])
    elif state[1]==0 and state[3] == 0 and not sign:
    	return  np.array([1, 1]) / np.sqrt(2),np.array([0., 1.])

    elif state[2]==0 and state[3] == 0 and sign:
    	return  np.array([1.,0.]) , np.array([1, 1]) / np.sqrt(2)
    elif state[2]==0 and state[3] == 0 and not sign:
    	return  np.array([1.,0.]) , np.array([1, -1]) / np.sqrt(2)

    else:
        print('The input state is an entangled state that cannot be separated')

def disable_all_buttons():
    for button in buttons:
        button.config(state="disabled")

def bell1():

	state = np.array([1,0,0,1])/np.sqrt(2)
	return state

def bell2():

	state = np.array([1,0,0,-1])/np.sqrt(2)
	return state

def bell3():

	state = np.array([0,1,1,0])/np.sqrt(2)
	return state

def bell4():

	state = np.array([0,1,-1,0])/np.sqrt(2)
	return state

def bells():

	states = [bell1(),bell2(),bell3(),bell4()]

	return states

def print_cmplx(z):
    
    re = np.real(z)
    im = np.imag(z)
    
    if re != 0 and im == 0:
        
        return f' {re:.1f}'
    
    elif re == 0 and im != 0:
        
        return f'j{im:.1f}'
    elif re == 0 and im == 0:
        
        return '0'


#def bell2text(entangle_state):

#	state_simil = []
#	for bell in bells():
#
#		state_simil.append(simil(entangle_state,bell))
#
#	state_simil = np.array(state_simil)
#	best_bell = np.argmax(state_simil)
#
#	return f"Bell {best_bell +1}"

def bell2text(entangle_state):

    p00 = entangle_state[0]
    p01 = entangle_state[1]
    p10 = entangle_state[2]
    p11 = entangle_state[3]

    return print_cmplx(p00) + ';' + print_cmplx(p01) + ';\n' + print_cmplx(p10) + ';' + print_cmplx(p11) 


def random_state():

	rand_num = random.randint(0,3)
	if rand_num == 0:
		result = np.array([1.,0.])
	elif rand_num == 1:
		result = np.array([0.,1.])
	elif rand_num == 2:
		result = np.array([1/np.sqrt(2),1/np.sqrt(2)])
	elif rand_num == 3:
		result = np.array([1/np.sqrt(2),-1/np.sqrt(2)])


	return result

def cmplx_print(a,rnd=2):
    
    re = np.real(a)
    im = np.imag(a)
    
    if re !=0. and im == 0.:
        
        string = f'{round(re,2)}'
    elif re ==0. and im != 0.:
        
        string = f'j{round(im,2)}'
    elif re !=0. and im != 0.:
        
        string = f'{round(re,2)} + j {round(im,2)}'
    elif re ==0. and im ==0.:
        
        string = '0'
    
    return string


def state2text(array):
	result=f'{cmplx_print(array[0])}\n{cmplx_print(array[1])}'
	return result

def state_toss(prob_ground):
    toss = random.random()
    
    if toss < prob_ground:
        return 0
    else:
        return 1

def entangle_state_toss(entangle_state):

	# (|00>, |01>, |10>, |11>) |Control, Target>
    entangle_state = abs(entangle_state)
    rand_num = random.uniform(0, sum(entangle_state))
    
    cumulative_sum = 0
    for i, coeff in enumerate(entangle_state):
        cumulative_sum += coeff
        if rand_num <= cumulative_sum:
            return i

def depolarizing_noise(error,state):

	error_prob = float(error)/100
	depolarized_state = (1 - error_prob) * state
	error_matrix = np.random.normal(0,error_prob/3,4).reshape((2,2))
	depolarized_state += (error_prob / 3) * np.matmul(error_matrix, state)

	# # Normalization
	depolarized_state /= np.linalg.norm(depolarized_state)

	print(depolarized_state[0]**2 + depolarized_state[1]**2)

	return depolarized_state

def b_click(button):

    global click_count, indx_control, indx_target,color_list,entangle_map,entangle_list, gate_noise
    
    gate_noise = spinbox_var.get()
    selected_operation = operation_var.get()
    selected_button = button.winfo_name()
    button_text = button.cget("text")
    indx = int(selected_button[0]) * 3 + int(selected_button[1])

    if selected_operation == "Y":
        state_list[indx] = depolarizing_noise(gate_noise,np.matmul(Y(), state_list[indx]))
        button.config(text=state2text(state_list[indx]))
    elif selected_operation == "H":
        state_list[indx] = depolarizing_noise(gate_noise,np.matmul(H(), state_list[indx]))
        button.config(text=state2text(state_list[indx]))
    elif selected_operation == "Z":
        state_list[indx] = depolarizing_noise(gate_noise,np.matmul(Z(), state_list[indx]))
        button.config(text=state2text(state_list[indx]))
    elif selected_operation == "X":
        state_list[indx] = depolarizing_noise(gate_noise,np.matmul(X(), state_list[indx]))
        button.config(text=state2text(state_list[indx]))
        print(state_list[indx][0]**2 + state_list[indx][1]**2)

    elif selected_operation == "CNOT":

        if click_count == 0 and button.cget('bg') == "SystemButtonFace":
            click_count += 1
            indx_control = indx
            button.config(bg=color_list[len(entangle_map)])

        elif click_count == 1 and button.cget('bg') == "SystemButtonFace":
            click_count = 0
            indx_target = indx
            button.config(bg=color_list[len(entangle_map)])
            state_ent = entangle(state_list[indx_control], state_list[indx_target])
            state_res = np.matmul(CNOT(), state_ent)
            if disentangle_check(state_res):
            	buttons[indx_control].config(bg="SystemButtonFace")
            	buttons[indx_target].config(bg="SystemButtonFace")
            else:
	            entangle_map.append((indx_control,indx_target))
	            entangle_list.append(state_res)
	            buttons[indx_control].config(text="C\n" + bell2text(state_res),font=('Tahoma',10))
	            buttons[indx_target].config(text="T\n" + bell2text(state_res))


        elif click_count == 0 and button.cget('bg') != "SystemButtonFace":

        	arr_ent_map = np.array(entangle_map)
        	try:
        		pair_index = np.where(arr_ent_map[:, 0] == indx )[0][0]
        		first_ctrl = True
        	except:
        		pair_index = np.where(arr_ent_map[:, 1] == indx )[0][0]
        		first_ctrl = False

        	pair = arr_ent_map[pair_index]
        	state_ent = entangle_list[pair_index]
        	state_res = np.matmul(CNOT(), state_ent)
        	print(state_res)
        	if not first_ctrl:
        		state_res[1] , state_res[2] = state_res[2], state_res[1]        	
        	print(state_res)
        	if disentangle_check(state_res):
	        	state_ctrl, state_targ = disentangle(state_res)
	        	del entangle_map[pair_index]
	        	del entangle_list[pair_index]
	        	state_list[pair[0]] = state_ctrl
	        	state_list[pair[1]] = state_targ
	        	buttons[pair[0]].config(text=state2text(state_ctrl))
	        	buttons[pair[1]].config(text=state2text(state_targ))
	        	buttons[pair[0]].config(bg="SystemButtonFace")
	        	buttons[pair[1]].config(bg="SystemButtonFace")
	        else:
	        	entangle_list[pair_index] = state_res


def measure():

	# Single qubit 

	for i in range(3):
		for j in range(3):
			indx = int(i)*3 + int(j)
			if buttons[indx].cget('bg') == "SystemButtonFace":
				p0 = state_list[indx][0]**2
				state_list[indx] = state_toss(p0)
				if state_list[indx] == 0:
					buttons[indx]['text'] = '0'
				elif state_list[indx] == 1:
					buttons[indx]['text'] = '1'

	# Entangled qubit

	for pair,entangle_state in zip(entangle_map,entangle_list):

		print(entangle_state)
		two_qubit_state = entangle_state_toss(entangle_state)

		print(two_qubit_state)

		if two_qubit_state == 0:

			buttons[pair[0]].config(text='0') 
			buttons[pair[1]].config(text='0')
			buttons[pair[0]].config(bg="SystemButtonFace") 
			buttons[pair[1]].config(bg="SystemButtonFace")
		elif two_qubit_state == 1:

			buttons[pair[0]].config(text='0') 
			buttons[pair[1]].config(text='1')
			buttons[pair[0]].config(bg="SystemButtonFace") 
			buttons[pair[1]].config(bg="SystemButtonFace")
		elif two_qubit_state == 2:

			buttons[pair[0]].config(text='1') 
			buttons[pair[1]].config(text='0')
			buttons[pair[0]].config(bg="SystemButtonFace") 
			buttons[pair[1]].config(bg="SystemButtonFace")
		elif two_qubit_state == 3:

			buttons[pair[0]].config(text='1') 
			buttons[pair[1]].config(text='1')
			buttons[pair[0]].config(bg="SystemButtonFace") 
			buttons[pair[1]].config(bg="SystemButtonFace")

	checkwhowon()
	disable_all_buttons()


def checkwhowon():
	points_gnd = 0
	points_exc = 0

	if buttons[0]["text"] == "0" and buttons[1]["text"] == "0" and buttons[2]["text"]  == "0":
		buttons[0].config(bg="red")
		buttons[1].config(bg="red")
		buttons[2].config(bg="red")
		points_gnd += 1

	if buttons[3]["text"] == "0" and buttons[4]["text"] == "0" and buttons[5]["text"]  == "0":
		buttons[3].config(bg="red")
		buttons[4].config(bg="red")
		buttons[5].config(bg="red")
		points_gnd += 1

	if buttons[6]["text"] == "0" and buttons[7]["text"] == "0" and buttons[8]["text"]  == "0":
		buttons[6].config(bg="red")
		buttons[7].config(bg="red")
		buttons[8].config(bg="red")
		points_gnd += 1

	if buttons[0]["text"] == "0" and buttons[3]["text"] == "0" and buttons[6]["text"]  == "0":
		buttons[0].config(bg="red")
		buttons[3].config(bg="red")
		buttons[6].config(bg="red")
		points_gnd += 1

	if buttons[1]["text"] == "0" and buttons[4]["text"] == "0" and buttons[7]["text"]  == "0":
		buttons[1].config(bg="red")
		buttons[4].config(bg="red")
		buttons[7].config(bg="red")
		points_gnd += 1

	if buttons[2]["text"] == "0" and buttons[5]["text"] == "0" and buttons[8]["text"]  == "0":
		buttons[2].config(bg="red")
		buttons[5].config(bg="red")
		buttons[8].config(bg="red")
		points_gnd += 1

	if buttons[0]["text"] == "0" and buttons[4]["text"] == "0" and buttons[8]["text"]  == "0":
		buttons[0].config(bg="red")
		buttons[4].config(bg="red")
		buttons[8].config(bg="red")
		points_gnd += 1

	if buttons[2]["text"] == "0" and buttons[4]["text"] == "0" and buttons[6]["text"]  == "0":
		buttons[2].config(bg="red")
		buttons[4].config(bg="red")
		buttons[6].config(bg="red")
		points_gnd += 1

	#### Excited state
	if buttons[0]["text"] == "1" and buttons[1]["text"] == "1" and buttons[2]["text"]  == "1":
		buttons[0].config(bg="blue")
		buttons[1].config(bg="blue")
		buttons[2].config(bg="blue")
		points_exc += 1

	if buttons[3]["text"] == "1" and buttons[4]["text"] == "1" and buttons[5]["text"]  == "1":
		buttons[3].config(bg="blue")
		buttons[4].config(bg="blue")
		buttons[5].config(bg="blue")
		points_exc += 1

	if buttons[6]["text"] == "1" and buttons[7]["text"] == "1" and buttons[8]["text"]  == "1":
		buttons[6].config(bg="blue")
		buttons[7].config(bg="blue")
		buttons[8].config(bg="blue")
		points_exc += 1

	if buttons[0]["text"] == "1" and buttons[3]["text"] == "1" and buttons[6]["text"]  == "1":
		buttons[0].config(bg="blue")
		buttons[3].config(bg="blue")
		buttons[6].config(bg="blue")
		points_exc += 1

	if buttons[1]["text"] == "1" and buttons[4]["text"] == "1" and buttons[7]["text"]  == "1":
		buttons[1].config(bg="blue")
		buttons[4].config(bg="blue")
		buttons[7].config(bg="blue")
		points_exc += 1

	if buttons[2]["text"] == "1" and buttons[5]["text"] == "1" and buttons[8]["text"]  == "1":
		buttons[2].config(bg="blue")
		buttons[5].config(bg="blue")
		buttons[8].config(bg="blue")
		points_exc += 1

	if buttons[0]["text"] == "1" and buttons[4]["text"] == "1" and buttons[8]["text"]  == "1":
		buttons[0].config(bg="blue")
		buttons[4].config(bg="blue")
		buttons[8].config(bg="blue")
		points_exc += 1

	if buttons[2]["text"] == "1" and buttons[4]["text"] == "1" and buttons[6]["text"]  == "1":
		buttons[2].config(bg="blue")
		buttons[4].config(bg="blue")
		buttons[6].config(bg="blue")
		points_exc += 1

	# Check if tie
	if points_gnd > points_exc:
		messagebox.showinfo("Qtris", f"Ground state wins with {points_gnd} points over {points_exc}!")
		disable_all_buttons()
	elif points_gnd < points_exc:
		messagebox.showinfo("Qtris", f"Excited state wins with {points_exc} points over {points_gnd}!")
		disable_all_buttons()
	elif points_gnd == points_exc:
		messagebox.showinfo("Qtris", f"It is a tie with {points_gnd} points to {points_exc}!")
		disable_all_buttons()


root = tk.Tk()
root.title("Button Operation Selector")

operation_var = tk.StringVar()
operation_var.set("X")

operation_label = tk.Label(root, text="Card:")
operation_label.grid(row=0, column=0, padx=10, pady=5)

operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=["Y","H","Z","X","CNOT","Cx"])
operation_dropdown.grid(row=0, column=1, padx=10, pady=5)

buttons = []
state_list = []
entangle_map = []
entangle_list = []
click_count = 0
color_list = ["#1E8F78","#5CAD55","#B4CF66","#DBCB4F"]

for i in range(3):
    for j in range(3):
        button = Button(root, text='', font=("Tahoma", 20), height=3, width=6, bg="SystemButtonFace",name=f'{i}{j}')
        state = random_state()
        state_list.append(state)
        button['text'] = state2text(state) 
        button.grid(row=i+1, column=j, padx=5, pady=5)
        button.config(command=lambda b=button: b_click(b))
        buttons.append(button)

# Add a spinbox for selecting a number
spinbox_var = tk.StringVar()
spinbox_label = tk.Label(root, text="Gate Noise:")
spinbox_label.grid(row=4, column=0, padx=10, pady=5)
spinbox = tk.Spinbox(root, from_=0, to=100, increment=1, textvariable=spinbox_var)
spinbox.grid(row=4, column=1, padx=10, pady=5)


# Add a button to trigger the measurement
measure_button = tk.Button(root, text="Measure", command=measure)
measure_button.grid(row=4, column=2, sticky="se", padx=10, pady=10)

root.mainloop()
