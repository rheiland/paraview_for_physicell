<div id="TOC">

</div>
<h1 id="introduction-and-citing-physicell">Introduction and citing PhysiCell </h1>
<p>This user guide will teach you how to download and use PhysiCell <span class="citation" data-cites="ref:PhysiCell"></span>, as well as document the key classes and functions. Wherever possible, it will demonstrate with specific examples. Please note that this guide will be periodically updated. Users should check <a href="http://PhysiCell.MathCancer.org">PhysiCell.MathCancer.org</a> for the latest version. The PhysiCell method paper was published in PLoS Computational Biology <span class="citation" data-cites="ref:PhysiCell"></span>.<br />
<br />
If you use PhysiCell, please cite it as:<br />
<br />
</p>
<p>We implemented and solved our model using PhysiCell (Version 1.7.1) [1].<br />
[1] A. Ghaffarizadeh, R. Heiland, S.H. Friedman, S.M. Mumenthaler, and P. Macklin. PhysiCell: an Open Source Physics-Based Cell Simulator for 3-D Multicellular Systems, PLoS Comput. Biol. 14(2): e1005991, 2018. DOI: <a href="https://dx.doi.org/10.1371/journal.pcbi.1005991">10.1371/journal.pcbi.1005991</a>.</p>
<p><br />
<br />
Because PhysiCell makes extensive use of BioFVM, we suggest you also cite it:</p>
<p>We implemented and solved the model using PhysiCell (Version 1.7.1) [1], with BioFVM [2] to solve the transport equations.<br />
[1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin. PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellular Systems, PLoS Comput. Biol. 14(2): e1005991, 2018. DOI: <a href="https://dx.doi.org/10.1371/journal.pcbi.1005991">10.1371/journal.pcbi.1005991</a><br />
[2] A Ghaffarizadeh, SH Friedman, and P Macklin. BioFVM: an efficient parallelized diffusive transport solver for 3-D biological simulations, Bioinformatics 32(8): 1256-8, 2016. DOI: <a href="https://dx.doi.org/10.1093/bioinformatics/btv730">10.1093/bioinformatics/btv730</a></p>
<p><strong>Please remember:</strong> if you use an additional addon, please make sure to cite it, too! This is critical for scientific rigor (to correctly document your method), reproducibility, and good academic behavior.</p>
<p>We have started testing methods to auto-generate suggested citations for addons; see the auto-generated CITATION.txt when you run your model. This will be further developed in future versions of PhysiCell.</p>

<h1 id="sec:getting_started">Getting started: The Quickstart and your First Simulation</h1>
<p>As of Version 1.2.2, every download of PhysiCell includes a <code>Quickstart.pdf</code> guide in the root directory. If you follow the instructions in that guide (along with instructions to set up your compiler and environment; see Section <a href="#sec:preparing_environment" data-reference-type="ref" data-reference="sec:preparing_environment">4</a>), you should be able to run and visualize your first PhysiCell simulation (heterogeneous tumor growth) in well under an hour.</p>
<p>You should also watch the <a href="https://twitter.com/search?f=tweets&amp;vertical=default&amp;q=PhysiCell&amp;src=typd">#PhysiCell hashtag</a> on Twitter for updates on PhysiCell and new tricks, tips, and tutorials. Tutorials and other blog posts can be found at <a href="http://mathcancer.org/blog/physicell-tutorials/">http://MathCancer.org/blog/physicell-tutorials/</a>. See Section <a href="#sec:blog_and_help" data-reference-type="ref" data-reference="sec:blog_and_help">3</a> for resources for help, including support tickets and the PhysiCell blog.</p>
<hr />
<h1 id="sec:blog_and_help">Further resources for help</h1>
<p>The PhysiCell project posts tips and tutorials at its blog:</p>
<div class="center">
<p><a href="http://www.mathcancer.org/blog/physicell-tutorials/">http://www.mathcancer.org/blog/physicell-tutorials/</a></p>
</div>
<p>Users are encouraged to frequently visit the blog for these tips. This user manual may be updated more frequently than PhysiCell. Please check the PhysiCell project website for updates:</p>
<div class="center">
<p><a href="http://PhysiCell.MathCancer.org">http://PhysiCell.MathCancer.org</a></p>
</div>
<p>Lastly, users can support help tickets at SourceForge:</p>
<div class="center">
<p><a href="https://sourceforge.net/p/physicell/tickets/">https://sourceforge.net/p/physicell/tickets/</a></p>
</div>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:preparing_environment">Preparing your development environment </h1>
<p>PhysiCell was designed to be cross-platform compatible, without need for a package manager system or any other complex installation. In principle, any <code>C++11</code> compliant compiler with OpenMP support should work. In practice, we use <code>g++</code> as our “gold standard.” You’ll also want to ensure that your build environment supports makefiles. Command-line zip/unzip is also helpful, but not required.</p>
<p>Please note that OSX (and its associated developer tools) ships with “<code>g++</code>” instead of <code>g++</code>: it uses LLVM/Clang and an alias to <em>pretend</em> to be <code>g++</code>. Unfortunately, the version of LLVM/Clang that Apple ships does not fully support OpenMP, and so compiling can fail on those platforms without further setup. For OSX, we recommend following our Homebrew-based tutorial to install real <code>g++</code>.</p>
<p>Full tutorials on installing a 64-bit <code>g++</code>/OpenMP environment (on Windows via mingw-w64 and on OSX using Homebrew) can be found at:</p>
<p><a href="http://www.mathcancer.org/blog/physicell-tutorials/">http://www.MathCancer.org/blog/physicell-tutorials/</a></p>
<p>Most linux users should already have a 64-bit <code>g++</code> environment installed by default.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:osx_setup_note">Special notes for OSX users</h2>
<p>As of Version 1.2.2, OSX users no longer need to modify the <code>CC</code> definition in the makefiles–this represents a significant simplification for those users. However, OSX users (including those who have already installed <code>g++</code> by Homebrew of MacPorts) need to perform a one-time setup of an environment variable. Open your terminal, and run the following commands:</p>
<pre><code>export PHYSICELL_CPP=your_compiler_name
echo export PHYSICELL_CPP=your_compiler_name &gt;&gt; ~/.bash_profile</code></pre>
<p><code>your_compiler_name</code> will be something like <code>g++-7</code> for Homebrew installations, and something like <code>g++-mp-7</code> for MacPorts installations.</p>
<p>See the tutorials at <a href="http://www.mathcancer.org/blog/physicell-tutorials/">http://www.MathCancer.org/blog/physicell-tutorials/</a> for more details. Also, if you have compiler crashes, see the FAQ (frequently asked questions) at:</p>
<p><a href="http://www.mathcancer.org/blog/common-problems-and-solutions/">http://www.mathcancer.org/blog/common-problems-and-solutions/</a></p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="virtual-machine-option">Virtual Machine option </h2>
<p>Starting with the 1.2.x releases, we began distributing PhysiCell as zipped source (preferred) and virtual appliances for use in <a href="http://virtualbox.org">VirtualBox</a> and other virtual machine software, allowing us to distribute a full PhysiCell development environment (including 64-bit <code>g++</code>, support for makefiles, zip/unzip, ImageMagick, mencoder, eog, a text editor, and the most up-to-date version of PhysiCell). This should make it simpler to start learning and using PhysiCell, even in cases where developers are not free to install or modify their own build environments, or have difficulty installing and configuring <code>g++</code>.</p>
<p>Please visit the <a href="http:/PhysiCell.MathCancer.org/blog/physicell-tutorials">PhysiCell blog</a> for information on running VirtualDub and using the virtual appliance. (Section <a href="#sec:blog_and_help" data-reference-type="ref" data-reference="sec:blog_and_help">3</a>).</p>
<p>Note that we do not update the Virtual Box distribution; you should download the latest PhysiCell version from inside your virtual machine.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="suggested-tutorials-and-resources">Suggested tutorials and resources</h2>
<p>Working in PhysiCell requires some knowledge of <code>C++</code>, Makefiles, and command-line routines in Unix-like systems. If you are not familiar with these skillsets, we recommend the following resources:</p>
<h3 id="linux-and-makefile-tutorials">Linux and Makefile tutorials</h3>
<ol>
<li><p><strong>A tutorial on learning the Linux shell:</strong> <a href="http://linuxcommand.org/lc3_learning_the_shell.php">http://linuxcommand.org/lc3_learning_the_shell.php</a><br />
In particular, I recommend:</p>
<ol>
<li><p><a href="http://linuxcommand.org/lc3_lts0010.php">What is “The Shell”?</a></p></li>
<li><p><a href="http://linuxcommand.org/lc3_lts0020.php">Navigation</a></p></li>
<li><p><a href="http://linuxcommand.org/lc3_lts0030.php">Looking Around</a></p></li>
<li><p><a href="http://linuxcommand.org/lc3_lts0050.php">Manipulating Files</a></p></li>
</ol></li>
<li><p><strong>UNIX Tutorial for Beginners:</strong> <a href="http://www.ee.surrey.ac.uk/Teaching/Unix/">http://www.ee.surrey.ac.uk/Teaching/Unix/</a><br />
In particular, I suggest the following:</p>
<ol>
<li><p><a href="http://www.ee.surrey.ac.uk/Teaching/Unix/unix1.html">Tutorial 1</a> (navigation, creating directories, etc.)</p></li>
<li><p><a href="http://www.ee.surrey.ac.uk/Teaching/Unix/unix2.html">Tutorial 2</a> (moving, copying files, etc.)</p></li>
<li><p><a href="http://www.ee.surrey.ac.uk/Teaching/Unix/unix4.html">Tutorial 4</a> (wildcards, filename conventions, etc.)</p></li>
<li><p><a href="http://www.ee.surrey.ac.uk/Teaching/Unix/unix7.html">Tutorial 7</a> (compiling and running software, etc.)</p></li>
<li><p><a href="http://www.ee.surrey.ac.uk/Teaching/Unix/unix8.html">Tutorial 8</a> (UNIX and environment variables, etc.) (<strong>Note:</strong> May not work in Windows/MinGW.)</p></li>
</ol></li>
<li><p><strong>The GNU Bash Reference Manual:</strong> <a href="http://www.gnu.org/software/bash/manual/bash.html">http://www.gnu.org/software/bash/manual/bash.html</a></p></li>
<li><p><strong>A good makefile tutorial:</strong> <a href="http://www.cprogramming.com/tutorial/makefiles.html">http://www.cprogramming.com/tutorial/makefiles.html</a></p></li>
<li><p><strong>Another good makefile tutorial:</strong> <a href="http://mrbook.org/blog/tutorials/make/">http://mrbook.org/blog/tutorials/make/</a></p></li>
<li><p><strong>One more makefile tutorial:</strong> <a href="http://makefiletutorial.com/">http://makefiletutorial.com/</a></p></li>
<li><p><strong>The GNU Make Reference:</strong> <a href="https://www.gnu.org/software/make/manual/make.html">https://www.gnu.org/software/make/manual/make.html</a></p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="c-references">C++ references</h3>
<p>The following websites are good references for <code>C++</code>:</p>
<ol>
<li><p><strong>CPlusPlus.com:</strong> <a href="http://www.cplusplus.com/">http://www.cplusplus.com/</a><br />
Excellent, detailed documentation on <code>C++</code>, as well as tutorials.</p></li>
<li><p><strong>C++ Reference:</strong> <a href="http://en.cppreference.com/w/">http://en.cppreference.com/w/</a><br />
Another good reference guide to <code>C++</code>.</p></li>
<li><p><strong>LearnCpp.com:</strong> <a href="http://www.learncpp.com/">http://www.learncpp.com/</a><br />
A series of tutorials on <code>C++</code>.</p></li>
<li><p><strong>StackOverflow (C++ tag):</strong> <a href="https://stackoverflow.com/questions/tagged/c%2b%2b">https://stackoverflow.com/questions/tagged/c%2b%2b</a><br />
A sometimes overwhelming resource for problem solving in <code>C++</code>.</p></li>
<li><p><strong>C++ section on CodeGuru:</strong> <a href="http://www.codeguru.com/cpp/cpp/">http://www.codeguru.com/cpp/cpp/</a></p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="matlab-tutorials">Matlab tutorials</h3>
<p>If you use Matlab for visualization and/or postprocessing, we recommend:</p>
<ol>
<li><p><strong>MATLAB tutorials at Mathworks:</strong> <a href="https://www.mathworks.com/academia/student_center/tutorials/mltutorial_launchpad.html">https://www.mathworks.com/academia/student_center/tutorials/mltutorial_launchpad.html</a></p></li>
<li><p><strong>Introduction to MATLAB for Engineering Students:</strong> <a href="https://www.mccormick.northwestern.edu/documents/students/undergraduate/introduction-to-matlab.pdf
">http://bit.ly/2cQBXDc</a></p></li>
<li><p><strong>A Beginner’s Guide to MATLAB:</strong> <a href="http://homen.vsb.cz/~lud0016/NM/matlab_guide.pdf">http://homen.vsb.cz/~lud0016/NM/matlab_guide.pdf </a><br />
(By Christos Xenophontos at Loyola College).</p></li>
<li><p><strong>MATLAB Academy:</strong> <a href="https://matlabacademy.mathworks.com/?s_eid=ppc_23223967642">https://matlabacademy.mathworks.com/?s_eid=ppc_23223967642</a></p></li>
<li><p><strong>MATLAB Tutorial:</strong> <a href="https://www.tutorialspoint.com/matlab/">https://www.tutorialspoint.com/matlab/</a></p></li>
<li><p><strong>Octave:</strong> If you do not have access to MATLAB or prefer an open source alternative, have a look at this cross-platform package:<br />
<a href="https://www.gnu.org/software/octave/">https://www.gnu.org/software/octave/</a></p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="virtualbox-and-related-information-virtual-appliances">VirtualBox and related information (virtual appliances)</h3>
<p>If you use the virtual appliance, we suggest the following tutorials and resources:</p>
<ol>
<li><p><strong>VirtualBox:</strong> <a href="http://virtualbox.org">http://virtualbox.org</a><br />
This is an excellent cross-platform (Windows, Linux, OSX, etc.) virtual machine software that can import the virtual appliance version of PhysiCell.</p></li>
<li><p><strong>Alpine Linux:</strong> <a href="https://alpinelinux.org/">https://alpinelinux.org/</a><br />
Alpine Linux is a lean and secure version of linux we installed in the PhysiCell virtual appliance.</p></li>
<li><p><strong>Alpine Linux Wiki:</strong> <a href="https://wiki.alpinelinux.org/">https://wiki.alpinelinux.org</a><br />
A helpful site for using Alpine Linux.</p></li>
<li><p><strong>VirtualBox shared folders in Alpine:</strong> <a href="https://wiki.alpinelinux.org/wiki/VirtualBox_shared_folders">https://wiki.alpinelinux.org/wiki/VirtualBox_shared_folders </a></p></li>
<li><p><strong>Alpine Linux users forum:</strong> <a href="https://forum.alpinelinux.org/
">https://forum.alpinelinux.org/ </a></p></li>
<li><p><strong>XFCE4 project:</strong> <a href="https://xfce.org/">https://xfce.org/</a><br />
We use the XFCE4 desktop environment in our virtual appliance, so this may be helpful.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="recommended-additional-tools">Recommended additional tools</h3>
<p>Lastly, we find the following tools and resources very useful for postprocessing and visualization:</p>
<ol>
<li><p><strong>ImageMagick</strong> is a cross-platform image manipulation suite, which can (among other things) resize and crop images, change formats, and insert text labels. In PhysiCell, ImageMagick is especially useful for converting SVG files to PNG, JPG, or other raster-based formats for further animation.</p>
<ul>
<li><p><strong>URL:</strong> <a href="http://imagemagick.org">http://imagemagick.org</a></p></li>
<li><p><strong>Typical use:</strong> <code>magick mogrify -format jpg snapshot*.svg</code><br />
(Converts all files of the form snapshot*.svg to the png format.)</p></li>
<li><p><strong>Typical use:</strong> <code>magick snapshot*.jpg animation.gif</code><br />
(Combines all snapshot*.jpg files into a (huge!) animated gif file.)</p></li>
</ul></li>
<li><p><strong>Mencoder</strong> is a cross-platform, open source mpeg encoder, useful for creating compressed movies. In PhysiCell, we use mencoder to convert series of simulation snapshots to movies.</p>
<ul>
<li><p><strong>URL (Linux):</strong> Use your package manager to install mplayer (which includes mencoder).</p></li>
<li><p><strong>URL (OSX):</strong> Use Homebrew or MacPorts to install mplayer (which includes mencoder).</p></li>
<li><p><strong>URL (Windows):</strong> <a href="http://mplayerwin.sourceforge.net/">http://mplayerwin.sourceforge.net/</a></p></li>
<li><p><strong>Typical use:</strong><br />
<code>mencoder "mf://snapshot*.jpg" -ovc lavc -lavcopts</code><br />
<code> vcodec=mpeg4:vbitrate=10000:mbd=2:trell -mf fps=24:type=jpg -nosound -o out.avi</code><br />
(Converts all the snapshot*.jpg files into an mpeg4-encoded movie named out.avi, with a 8kbps variable bit rate and 24 frames per second.)</p></li>
</ul></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h1 id="overall-codebase-structure">Overall codebase structure </h1>
<p>PhysiCell was created by extending the <code>Basic_Agent</code> class in BioFVM <span class="citation" data-cites="ref:BioFVM"></span> to include a fuller cell phenotype and force-based cell motion. In the overall software philosophy, we structure PhysiCell in several critical subdirectories:</p>
<ol>
<li><p><strong><code>BioFVM</code></strong> This includes a working copy of the BioFVM multi-substrate diffusion code <span class="citation" data-cites="ref:BioFVM"></span>. Users should be able to fully replace these files with any later version of BioFVM. Note that BioFVM distributions also include pugixml (an efficient cross-platform XML parser) <span class="citation" data-cites="ref:pugixml"></span>.</p></li>
<li><p><strong><code>beta</code></strong> This directory is used for beta functionality used by our team during testing and development. Use at your own risk!</p></li>
<li><p><strong><code>config</code></strong> This directory is used for XML configuration files with. Any custom configuration files should be placed in this directory.</p></li>
<li><p><strong><code>core</code></strong> The core library files for PhysiCell are kept in this directory. Users should not modify functions in the core library.</p></li>
<li><p><strong><code>custom_modules</code></strong> This directory is the right place to put custom user code. Moreover, users should list their custom code files in <code>custom_modules/PhysiCell_custom.h</code>.</p></li>
<li><p><strong><code>modules</code></strong> This is where we place non-core (but helpful) standard code modules for distribution with PhysiCell. Currently, we include pathology, MultiCellDS <span class="citation" data-cites="ref:MultiCellDS"></span>, and SVG (scalable vector graphic) functions. Future releases may include basic modules for extracellular matrix.</p></li>
</ol>
<p>The following subdirectories are also included:</p>
<ol>
<li><p><strong><code>archives</code></strong> If you use the <code>make zip</code> or <code>make archive</code> rules, the compressed archives will be placed here.</p></li>
<li><p><strong><code>documentation</code></strong> This directory includes user guides (like this one!).</p></li>
<li><p><strong><code>matlab</code></strong> This includes basic Matlab files for handling PhysiCell outputs. (This and other postprocessing will be a major PhysiCell focus over the next few years.)</p></li>
<li><p><strong><code>examples</code></strong> The examples from the PhysiCell method paper will be placed here. They may not necessarily be updated for compatibiltiy with every PhysiCell release. (They are currently compatible up to version 1.1.1.)</p></li>
<li><p><strong><code>licenses</code></strong> License files for BioFVM <span class="citation" data-cites="ref:BioFVM"></span>, pugixml <span class="citation" data-cites="ref:pugixml"></span>, PhysiCell, and any other (BSD-compatible) dependencies are kept here.</p></li>
<li><p><strong><code>output</code></strong> Some examples will put their outputs here.</p></li>
<li><p><strong><code>povray</code></strong> This includes some basic utilities for visualization by povray (an open source raytracing package) <span class="citation" data-cites="ref:povray"></span>.</p></li>
<li><p><strong><code>sample_projects</code></strong> This directory includes sample projects, including 2D and 3D template projects and at least the four sample projects in <span class="citation" data-cites="ref:PhysiCell"></span>. A good start to a new project is to use the <code>make template2D</code> or <code>make template3D</code> makefile rules, which will populate the <code>main.cpp</code>, <code>Makefile</code>, and <code>./custom_modules</code> with appropriate codes to get started. See Section <a href="#sec:templates" data-reference-type="ref" data-reference="sec:templates">6</a> for more information on the template projects, and Section <a href="#sec:sample_projects" data-reference-type="ref" data-reference="sec:sample_projects">7</a> for the full list of sample projects and instructions to build them.</p></li>
</ol>
<h2 id="sec:time_steps">Time step sizes in PhysiCell</h2>
<p>PhysiCell uses three time step sizes:</p>
<ol>
<li><p><code>diffusion_dt</code> is the step size used in the diffusion solver, including the secretion/export and uptake processes. The default value is 0.01 min.</p></li>
<li><p><code>mechanics_dt</code> is the step size for the cell mechanics solver, including cell motility. Each cell’s custom function is also evaluated on this time scale. The default value is 0.1 min.</p></li>
<li><p><code>phenotype_dt</code> is the step size for phenotype processes (e.g., cycle progression, volume changes). The default value is 6 min.</p></li>
</ol>
<p>As of PhysiCell 1.6.1, these values can be set in the XML configuration file. See Section <a href="#sec:XML_PhysiCell_structure" data-reference-type="ref" data-reference="sec:XML_PhysiCell_structure">13.3</a>.</p>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:templates">Using project templates </h1>
<p>As of Version 1.1.0, PhysiCell includes templates for 2-D and 3-D projects. These template projects set up all the critical BioFVM (microenvironment) and PhysiCell data structures and give examples on seeding a few cells. When beginning a new project with PhysiCell, we strongly recommend starting with these templates.</p>
<p>To start a new 2-D project (based on the template), go to the command line in the root PhysiCell directory, and run:</p>
<p><code>make template2D</code></p>
<p>This will populate a starting project from the files in <code>./sample_projects/template2D/</code>. In particular, it will overwrite the <code>Makefile</code>, copy <code>template_projects/template2D.cpp</code> to <code>main.cpp</code> in the root directory, and copy the contents of <code>./sample_projects/template2D/custom_modules/</code> to <code>./custom_modules</code>. Note that the <code>Makefile</code> has been modified to include the custom modules:</p>
<pre><code># put your custom objects here (they should be in the custom_modules directory)

PhysiCell_custom_module_OBJECTS := custom.o

##### and later in the Makefile ... 

# user-defined PhysiCell modules

custom.o: ./custom_modules/custom.cpp 
    $(COMPILE_COMMAND) -c ./custom_modules/custom.cpp</code></pre>
<p>In general, your project should modify main.cpp, but primarily add custom codes to <code>./custom_modules</code>, just as this example. (For example, you might define your own angiogenesis functions in <code>./custom_modules/angiogenesis.h</code>, implement the functions in <code>./custom_modules/angiogenesis.cpp</code>, and then modify the <code>Makefile</code> to include it:</p>
<pre><code># put your custom objects here (they should be in the custom_modules directory)

PhysiCell_custom_module_OBJECTS := custom.o angiogenesis.o

##### and later in the Makefile ... 

# user-defined PhysiCell modules

custom.o: ./custom_modules/custom.cpp 
    $(COMPILE_COMMAND) -c ./custom_modules/custom.cpp

angiogenesis.o: ./custom_modules/angiogenesis.cpp 
    $(COMPILE_COMMAND) -c ./custom_modules/angiogenesis.cpp</code></pre>
<p>This is the recommended structure for a project.</p>
<p>Once you’re ready, build the project by typing</p>
<p><code>make</code></p>
<p>By default, the executable will be called <code>project2D</code> (<code>project2D.exe</code> on windows). To change the name of the executable, modify the <code>PROJECT_NAME</code> variable in the <code>Makefile</code>.</p>
<p>To start a new 3-D project based on a template, type <code>make template3D</code> and continue as before.</p>
<p>Now, run the code:</p>
<p><code>./project2D</code></p>
<p>(in Windows, omit the “<code>./</code>”.) This will generate (among other things) a series of <a href="https://en.wikipedia.org/wiki/Scalable_Vector_Graphics">SVG</a> images that visualize the simulation once per hour.</p>
<p>More examples will be introduced on the PhysiCell blog. See Section <a href="#sec:blog_and_help" data-reference-type="ref" data-reference="sec:blog_and_help">3</a>.</p>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:sample_projects">Using the Sample Projects</h1>
<p>PhysiCell includes several sample projects to illustrate capabilities and suggest modeling possibilities. In general, building and running these projects consists of the following steps:</p>
<ol>
<li><p><strong>Populate a project:</strong> Use the following Makefile rule (from a terminal / command project in your PhysiCell root directory):</p>
<p><code>make [project_name]</code></p>
<p>where <code>[project_name]</code> is one of the sample projects listed below. For example, to populate the “cancer biorobots” sample project:</p>
<p><code>make cancer-biorobots-sample</code></p></li>
<li><p><strong>Build the project:</strong> Just run make:</p>
<p><code>make</code></p></li>
<li><p><strong>Run the project:</strong> Run the executable created by the compiler. If the name of the program is <code>[PROGRAM_NAME]</code>, run</p>
<p><code>./[PROGRAM_NAME]</code></p>
<p>(Windows users should omit the <code>./</code>.)</p>
<p>One simple way to determine the name of the executable is to use grep on the Makefile:</p>
<p><code>grep PROGRAM_NAME Makefile</code></p>
<p>For example, to run the cancer biorobots example, the executable name is <code>cancer_biorobots</code>, so you run:</p>
<p><code>./cancer_biorobots</code></p>
<p>The project will create a series of SVG images files, as well as MultiCellDS save files (a combination of matlab and XML files). See <a href="#sec:matlab_data" data-reference-type="ref" data-reference="sec:matlab_data">14.2.1</a> and the PhysiCell blog.</p></li>
<li><p><strong>(Optional) Clear out the project / return to a clean slate:</strong> If you want to build and run a different sample project, or clear out the sample materials to create your own, you need to “de-populate” the sample project:</p>
<p><code>make reset</code></p></li>
</ol>
<p>Here are the sample projects included as of Version 1.2.2:</p>
<ol>
<li><p><strong><code>biorobots-sample</code></strong> is a 2-D example of 3 cell types: cargo cells, worker cells (which seek out cargo cells and haul them to a destination), and director cells (which attract worker cells).</p></li>
<li><p><strong><code>cancer-biorobots-sample</code></strong> extends the biorobots example to (1) simulate a 2-D tumor that develops a necrotic core, (2) so that cargo cells are hauled towards hypoxic tumor regions, and (3) so that released cargo cells secrete a chemotherapeutic compounds.</p></li>
<li><p><strong><code>heterogeneity-sample</code></strong> simulates a 2-D tumor with heterogeneous “genetics” that drive differential proliferation.</p></li>
<li><p><strong><code>cancer-immune-sample</code></strong> extends the heterogeneity example to 3D, and introduces a new immune cell type (modeling T cells) that migrate towards tumor cells, temporarily adhere, test for immunogenicity, and initiate apoptosis.</p></li>
<li><p><strong><code>virus-macrophage-sample</code></strong> simulates a basic virus that diffuses, is uptaken by cells, replicates, and then is released in cell lysis. Macrophages eat and degrade infected cells. This is a test of internalized substrate tracking first released in PhysiCell 1.5.0.</p></li>
<li><p><strong><code>beta-testing</code></strong> is a small project that can be used for beta testing new features. Don’t count on it remaining unchanged from release to release.</p></li>
<li><p><strong><code>template2D</code></strong> is the template for a 2-D project. See Section <a href="#sec:templates" data-reference-type="ref" data-reference="sec:templates">6</a>.</p></li>
<li><p><strong><code>template3D</code></strong> is the template for a 3-D project. See Section <a href="#sec:templates" data-reference-type="ref" data-reference="sec:templates">6</a>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:makefiles">Extra makefile rules</h2>
<p>To clear out the data generated in a simulation:</p>
<p><code>make data-cleanup</code></p>
<p>To clear out the compiler-generated objects (which would allow you to recompile the entire project):</p>
<p><code>make clean</code></p>
<p>To reset to a clean slate (e.g., to clear out a sample project and populate another):</p>
<p><code>make reset</code></p>
<p>To get a list of all sample projects:</p>
<p><code>make list-projects</code></p>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:BioFVM">The BioFVM microenvironment</h1>
<p>PhysiCell is built upon BioFVM <span class="citation" data-cites="ref:BioFVM"></span>, and so it uses the (bio)chemical microenvironment from BioFVM, including diffusion, decay, cell-based secretions/export/uptake, and bulk supply/uptake functions. All PhysiCell projects already include bioFVM once you have included PhysiCell:</p>
<p><code>#include "./core/PhysiCell.h"</code></p>
<p>We also suggest using the BioFVM and PhysiCell namespaces:</p>
<pre><code>using namespace BioFVM;
using namespace PhysiCell;</code></pre>
<h2 id="sec:about_BioFVM_microenvironment">Notes on the microenvironment</h2>
<p>BioFVM divides the simulation domain into a collection of non-intersecting <strong>voxels</strong>: volumetric pixels. Each voxel has a unique integer <strong>index</strong>: this is its unique address, for quickly accessing its information. As particularly notable information, each voxel stores its own position (center) and volume.</p>
<p>BioFVM adds one or more diffusible substrates to this microenvironment. Each substrate has a diffusion coefficient and decay rate. At present, these are homogeneous throughout the microenvironment, although improvements are planned for BioFVM to have spatially variable diffusion coefficients. In BioFVM, each substrate diffuses and decays, and can be secreted or uptaken by individual cells (see Section <a href="#sec:Secretion" data-reference-type="ref" data-reference="sec:Secretion">11.7</a>) at their individual positions. As of PhysiCell 1.5.0, each cell can track the total amount of each substrate secreted and uptaken, and pass half of it contents to its two daughter cells at division. Users can optionally set PhysiCell to release the cell’s internalized substrates at the end of death or lysis. You can also set bulk uptake and secretion functions, which are applied in each voxel. These are not used in the current template and sample PhysiCell projects. See <span class="citation" data-cites="ref:BioFVM"></span> for more information.</p>
<p>For each voxel, we store a vector of chemical substrates (densities), and a vector of gradients (one gradient vector for each substrate). Moreover, users can use “Dirichlet nodes” to overwrite the substrate values at any voxel within the simulation domain. This is useful for modeling biotransport in irregular domains, setting substrate values along blood vessels, or applying classical Dirichlet conditions along the outer edges of the simulation domain. Note that without specifying Dirichlet conditions, BioFVM applies Neumann (no flux) conditions at the outer simulation boundaries.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:biotransport_equations">Biotransport equations</h3>
<p>Based upon BioFVM <span class="citation" data-cites="ref:BioFVM"></span>, PhysiCell solves the following system of partial differential equations (PDEs):</p>
<p><span class="math display">$$\frac{ \partial \boldsymbol{\rho}}{\partial t} 
= \mathbf{D} \circ \nabla^2 \boldsymbol{\rho} - \boldsymbol{\lambda} \circ \boldsymbol{\rho} + \sum_i \delta \left( \mathbf{x} - \mathbf{x}_i \right) 
\Bigl[ V_i \mathbf{S}_i \circ \left( \boldsymbol{\rho}^*_i - \boldsymbol{\rho} \right) - V_i \mathbf{U}_i \circ \boldsymbol{\rho} + \mathbf{E}_i \Bigr],$$</span> where</p>
<div class="center">
<table>
<thead>
<tr class="header">
<th style="text-align: center;"><strong>Symbol</strong></th>
<th style="text-align: left;">Meaning</th>
<th style="text-align: left;">Dimensions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"><span class="math inline">$\rho\hspace{-5.1pt}\rho$</span></td>
<td style="text-align: left;">vector of substrate densities (or concentrations)</td>
<td style="text-align: left;">substance/volume</td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><strong>D</strong></span></td>
<td style="text-align: left;">vector of diffusion coefficients</td>
<td style="text-align: left;">length<span class="math inline"><sup>2</sup></span>/time</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><span class="math inline"><strong>λ</strong></span></td>
<td style="text-align: left;">vector of decay rates</td>
<td style="text-align: left;">1/time</td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><em>V</em><sub><em>i</em></sub></span></td>
<td style="text-align: left;">volume of cell <span class="math inline"><em>i</em></span></td>
<td style="text-align: left;">volume</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><span class="math inline"><strong>x</strong><sub><em>i</em></sub></span></td>
<td style="text-align: left;">cell <span class="math inline"><em>i</em></span>’s position (center)</td>
<td style="text-align: left;">length</td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><strong>S</strong><sub><em>i</em></sub></span></td>
<td style="text-align: left;">vector of cell <span class="math inline"><em>i</em></span>’s secretion rates</td>
<td style="text-align: left;">1/time</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><span class="math inline"><strong>ρ</strong><sub><em>i</em></sub><sup>*</sup></span></td>
<td style="text-align: left;">vector of cell <span class="math inline"><em>i</em></span>’s secretion saturations</td>
<td style="text-align: left;">substance/volume</td>
</tr>
<tr class="even">
<td style="text-align: center;"><span class="math inline"><strong>U</strong><sub><em>i</em></sub></span></td>
<td style="text-align: left;">vector of cell <span class="math inline"><em>i</em></span>’s uptake rates</td>
<td style="text-align: left;">1/time</td>
</tr>
<tr class="odd">
<td style="text-align: center;"><span class="math inline"><strong>E</strong><sub><em>i</em></sub></span></td>
<td style="text-align: left;">vector of cell <span class="math inline"><em>i</em></span>’s net export rates</td>
<td style="text-align: left;">substance/time</td>
</tr>
</tbody>
</table>
</div>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:set_up_BioFVM">Setting up and using the microenvironment</h2>
<h3 id="sec:BioFVM_setup_XML">Specifying the microenvironment via XML ()</h3>
<p>As of PhysiCell version 1.6.0, the chemical microenvironment can be completely set up via the XML configuration file. (See also Section <a href="#sec:XML_PhysiCell_structure" data-reference-type="ref" data-reference="sec:XML_PhysiCell_structure">13.3</a> to learn about the XML structure.) This is now the preferred method of setting up the chemical microenvironment, as it can be done without recompiling a PhysiCell application and it provides easy access to modify the physical parameters (diffusion and decay rates), boundary conditions, and initial conditions.</p>
<p>See Section <a href="#sec:XML_microenvironment_setup" data-reference-type="ref" data-reference="sec:XML_microenvironment_setup">13.4</a> for full documentation, including examples.</p>
<p>All these properties can also be manually edited within a PhysiCell project via the C++ commands in Section <a href="#sec:BioFVM_manual_setup_options" data-reference-type="ref" data-reference="sec:BioFVM_manual_setup_options">8.2.2</a>.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:BioFVM_manual_setup_options">Manual configuration via C++ function calls ()</h3>
<p>Within your main program loop (<code>int main( int argc, char* argv[])</code>), you need to declare and set up a Microenvironment. (Here, we also include some useful tips for setting space and time units.) We make use of BioFVM 1.1.5 improvements that include simplified setup functions.</p>
<h4 id="sec:BioFVM_options">Setting BioFVM options</h4>
<p>BioFVM 1.1.5 and later versions includes a data structure (<code>default_microenvironment_options</code>, of type <code>Microenvironment_Options</code>) for setup options. This data type is defined in <code>BioFVM_microenvironment.h</code> as:</p>
<pre><code>class Microenvironment_Options
{
 private:
 
 public: 
    Microenvironment* pMicroenvironment;
    std::string name; 
 
    std::string time_units; 
    std::string spatial_units; 
    double dx;
    double dy; 
    double dz; 
    
    bool outer_Dirichlet_conditions; 
    std::vector&lt;double&gt; Dirichlet_condition_vector; 
    std::vector&lt;bool&gt; Dirichlet_activation_vector; 

    std::vector&lt;double&gt; initial_condition_vector; 

    bool simulate_2D; 
    std::vector&lt;double&gt; X_range; 
    std::vector&lt;double&gt; Y_range; 
    std::vector&lt;double&gt; Z_range; 
    
    Microenvironment_Options(); 
    
    bool calculate_gradients; 
    
    bool use_oxygen_as_first_field;
    
    bool track_internalized_substrates_in_each_agent;   
};</code></pre>
<p>You can set these options either towards the top of your main program source file (e.g., in <code>main.cpp</code>) or in a standalone setup function. See the sample projects for examples. Here is sample use, to set the tissue name to “liver” and set up to 3D with Dirichlet conditions of oxygen = 38 mmHg:</p>
<pre><code>/* Microenvironment setup */ 

default_microenvironment_options.name = &quot;liver&quot;; 
default_microenvironment_options.time_units = &quot;min&quot;; 
default_microenvironment_options.spatial_units = &quot;micron&quot;; 
default_microenvironment_options.dx = 20; 
default_microenvironment_options.dy = 20;  
default_microenvironment_options.dz = 20; 
    
// set a Dirichlet outer boundary condition 
default_microenvironment_options.outer_Dirichlet_conditions = true;

std::vector&lt;double&gt; bc_vector( 1 , 38.0 ); // 5% o2  
default_microenvironment_options.Dirichlet_condition_vector = bc_vector; 

// set the initial oxygen concentration (uniform in the domain) at 42 mmHg: 
default_microenvironment_options.initial_condition_vector = {42.0 }; 
    
// stick with a 3-D simulation 
default_microenvironment_options.simulate_2D = false; 

// set the domain size 
default_microenvironment_options.X_range = {-500, 500};  
default_microenvironment_options.Y_range = {-400, 400}; 
default_microenvironment_options.Z_range = {-100, 100}; 
    
// turn off gradient calculations 
default_microenvironment_options.bool calculate_gradients = false; 

// track internalized oxygen 
default_microenvironment_options.track_internalized_substrates_in_each_agent = true; </code></pre>
<div class="center">
<hr />
<hr />
</div>
<h4 id="sec:BioFVM_add_substrates">Adding new diffusing substrates to the tissue environment</h4>
<p>By default, the BioFVM microenvironment has a single substrate (with index 0). To add (append) a new substrate to the microenvironment, use one of these functions:</p>
<ol>
<li><p><strong><code>void Microenvironment::add_density( void )</code></strong> Use this to add a new diffusing substrate (density), without setting any of its properties.</p></li>
<li><p><strong><code>void Microenvironment::add_density( std::string name , std::string units )</code></strong> Use this to add a new substrate called <code>name</code> with units <code>units</code>. (e.g., crayons with units Megacrayolas).</p></li>
<li><p><strong><code>void Microenvironment::add_density( std::string name , std::string units, double diffusion_constant, double decay_rate )</code></strong> acts similarly as above, but also sets the diffusion coefficient and decay rate. Generally, these should be in the same units as the simulation: by default, <span class="math inline"><em>μ</em>m<sup>2</sup>/min</span> for diffusion and <span class="math inline">1/min</span> for decay.</p></li>
</ol>
<p>You can also change the name, units, and properties for an existing substrate:</p>
<ol>
<li><p><strong><code>void Microenvironment::set_density( int index , std::string name , std::string units )</code></strong> This function renames the substrate with index <code>index</code> to <code>name</code>, and sets its units to <code>units</code>.</p></li>
<li><p><strong><code>void Microenvironment::set_density( int index , std::string name , std::string units , double diffusion_constant , double decay_rate )</code></strong> works as above, but also sets the diffusion coefficient and decay rate.</p></li>
</ol>
<p>For example,</p>
<pre><code>// add a chemoattractant 

microenvironment.add_density( &quot;chemoattractant&quot;, &quot;dimensionless&quot; ); 
microenvironment.diffusion_coefficients[1] = 1e3; 
microenvironment.decay_rates[1] = .1;   
    
// add a therapeutic compound
    
microenvironment.add_density( &quot;drug&quot;, &quot;dimensionless&quot; ); 
microenvironment.diffusion_coefficients[2] = 1e3; 
microenvironment.decay_rates[2] = 0.15625;  
    
// rename the first density to be glucose, and change parameters 
    
microenvironment.set_density(0, &quot;glucose&quot;, &quot;dimensionless&quot; ); 
microenvironment.diffusion_coefficients[0] = 1e3; 
microenvironment.decay_rates[0] = 0.05625;  </code></pre>
<p>You should always add or modify your substrates prior to initializing the microenvironment. See Section <a href="#sec:BioFVM_initialize" data-reference-type="ref" data-reference="sec:BioFVM_initialize">8.2.2.3</a></p>
<div class="center">
<hr />
<hr />
</div>
<h4 id="sec:BioFVM_initialize">Initializing the BioFVM tissue microenvironment</h4>
<pre><code>// initialize BioFVM with these options
initialize_microenvironment();  </code></pre>
<p>BioFVM defaults to a 1 mm<span class="math inline"><sup>3</sup></span> domain centered at (0,0,0) with <span class="math inline"><em>Δ</em><em>x</em> = <em>Δ</em><em>y</em> = <em>Δ</em><em>z</em> = 20 <em>μ</em>m</span>, simulating 3D with no Dirichlet conditions and no gradient calculations, and minutes time units and micron space units. If you call <code>initialize_microenvironment()</code> without setting units (see Section <a href="#sec:BioFVM_options" data-reference-type="ref" data-reference="sec:BioFVM_options">8.2.2.1</a>), these defaults will be used.</p>
<p>The code also automatically chooses the correct 2D/3D diffusion solver, and sets the single diffusing field to oxygen with diffusion coefficient <span class="math inline">10<sup>5</sup><em>μ</em>m<sup>2</sup>/min</span> and decay coefficient <span class="math inline">0.1 1/min</span> (for a 1 mm diffusion length scale in the absence of cells).</p>
<p>By the end of these commands, the default <code>Microenvironment</code> is set to <code>microenvironment</code>. You can get this address at any time using the BioFVM command:</p>
<p><code>Microenvironment* get_default_microenvironment( void )</code></p>
<p>You’ll also need to set up PhysiCell’s mechanics data structures (for cell-cell interaction testing) and match them to BioFVM:</p>
<pre><code>/* PhysiCell setup */ 

// prepare PhysiCell mechanics data structures 

// mechanics voxel size 
double mechanics_voxel_size = 30; 
Cell_Container* cell_container = create_cell_container_for_microenvironment( 
   microenvironment, mechanics_voxel_size );</code></pre>
<p>Within your main program loop, you’ll want to make sure that BioFVM is being called to update the biochemical environment:</p>
<pre><code>while( t &lt; t_max )
{
   // main loop contents ... 

   // update the microenvironment
  
   microenvironment.simulate_diffusion_decay( diffusion_dt );
   // No longer needed as of BioFVM 1.3.1. Gradients 
   // are automaticaly calculated in the update_all_cells() 
   // function, as needed. 
   // if( default_microenvironment_options.calculate_gradients )
   // { microenvironment.compute_all_gradient_vectors(); }   
   
   // physicell functions 
  
   t += diffusion_dt; 
}</code></pre>
<p>As of Version 1.2.0, PhysiCell has automated cell secretions/export/uptake as part of its phenotype updates. There is no need to explicitly call the BioFVM cell-based functions in the main program loop.</p>
<p>As of Version 1.3.1, PhysiCell has automated calculation of gradients once per <span class="math inline"><em>Δ</em><em>t</em><sub>mechanics</sub></span> within the <code>update_all_cells()</code> functions. Users no longer need to explicitly calculate gradients. Just make sure you enable them in your setup, via:</p>
<pre><code>default_microenvironment_options.calculate_gradients = true; </code></pre>
<p>Note that the PhysiCell template projects and sample projects already include these critical setup commands. See Section <a href="#sec:templates" data-reference-type="ref" data-reference="sec:templates">6</a>.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:sample_microenvironment">Sampling the microenvironment</h2>
<p>To make it easier to write functions involving microenvironment substrates at any cell’s location, BioFVM 1.1.5 added the following function:</p>
<p><strong><code>int Microenvironment::find_density_index( std::string name )</code></strong> This allows you to find the index of the substrate named <code>name</code>. Note that this function is case sensitive.</p>
<p>The following functions can access the substrates and their gradients in space:</p>
<p><strong><code>int nearest_voxel_index( std::vector&lt;double&gt;&amp; position )</code></strong> This returns the integer that identifies the microenvironment voxel containing the point at <code>position</code>.</p>
<p><strong><code>std::vector&lt;double&gt;&amp; nearest_density_vector( std::vector&lt;double&gt;&amp; position )</code></strong> This function returns the vector of substrates located nearest to <code>position</code>.</p>
<p><strong><code>std::vector&lt;double&gt;&amp; nearest_density_vector( int voxel_index )</code></strong> This function returns the vector of substrates stored in the voxel with index <code>voxel_index</code>. See the <code>nearest_voxel_index</code></p>
<p><strong><code>std::vector&lt;double&gt;&amp; operator()( int n )</code></strong> This function can directly access the density vector stored at voxel index <code>n</code>.</p>
<p><strong><code>std::vector&lt;gradient&gt;&amp; gradient_vector(int n )</code></strong> This function accesses the vector of gradient vectors at voxel index <code>n</code>.</p>
<p><strong><code>std::vector&lt;gradient&gt;&amp; gradient_vector(std::vector&lt;double&gt;&amp; position )</code></strong> This function accesses the vector of gradient vectors at <code>position</code>.</p>
<p>Here’s an example of these functions in action:</p>
<pre><code>bool bad_conditions( Microenvironment&amp; M , int voxel_index )
{
    // find the correct indices the first time you run this function
    static int oxygen_index  = M.find_density_index( &quot;oxygen&quot; ); 
    static int glucose_index = M.find_density_index( &quot;glucose&quot; ); 

    // find the oxygen gradient 
    
    std::vector&lt;double&gt; gradient = M.gradient_vector(voxel_index)[oxygen_index]; 

    static double oxygen_threshold = 2.5; // mmHg 
    static double glucose_threshold = 0.05; // dimensionless 
 
    if( M(voxel_index)[oxygen_index]  &lt; oxygen_threshold &amp;&amp; 
        M(voxel_index)[glucose_index] &lt; glucose_threshold )
    { return true; }
    
    return false; 
}</code></pre>
<p>There are several functions to help sample the microenvironment at a cell’s position. See Section <a href="#sec:Cells" data-reference-type="ref" data-reference="sec:Cells">9</a>.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Dirichlet">Dirichlet conditions</h2>
<p>BioFVM also allows you to set constant conditions at any voxel. (These are called Dirichlet nodes.) The relevant functions are:</p>
<ol>
<li><p><strong><code>void Microenvironment::add_dirichlet_node( int voxel_index, std::vector&lt;double&gt;&amp; value )</code></strong> adds a Dirichlet node at voxel <code>voxel_index</code>, so that (for some <code>Microenvironment M</code>):</p>
<p><code>M(voxel_index) = value</code>.</p></li>
<li><p><strong><code>void Microenvironment::update_dirichlet_node( int voxel_index , std::vector&lt;double&gt;&amp; new_value )</code></strong> overwrites the (vector) value of the Dirichlet node at <code>voxel_index</code>, so that</p>
<p><code>M(voxel_index) = new_value</code>.</p>
<p>If the voxel was not previously a Dirichlet node, it is automatically changed to a Dirichlet node.</p></li>
<li><p><strong><code>void Microenvironment::update_dirichlet_node( int voxel_index , int substrate_index , double new_value )</code></strong> can be used to update a single substrate’s dirichlet condition at specific voxel, rather than all of them.</p></li>
<li><p><strong><code>void Microenvironment::remove_dirichlet_node( int voxel_index )</code></strong> removes the Dirichlet node at voxel <code>voxel_index</code>.</p></li>
<li><p><strong><code>void Microenvironment::apply_dirichlet_conditions( void )</code></strong> applies the previously set Dirichlet conditions at all Dirichlet nodes.</p></li>
<li><p><strong><code>bool&amp; Microenvironment::is_dirichlet_node( int voxel_index )</code></strong> returns <code>true</code> if there is a Dirichlet node at voxel <code>voxel_index</code>.</p></li>
</ol>
<p>BioFVM applies these Dirichlet conditions every time it evaluates the diffusion solver.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:refined_Dirichlet_conditions">Refined control of Dirichlet conditions</h3>
<p>As of Version 1.2.1, you can now control Dirichlet conditions on a substrate-by-substrate basis. That is, you can apply the Dirichlet condition to just one or two substrates (e.g., oxygen in index 0 and doxorubicin in index 12), while not applying them to the remaining substrates. For a microenvironment <code>M</code>, you can set these options in the <code>default_microenvironment_options</code> (see Section <a href="#sec:BioFVM_options" data-reference-type="ref" data-reference="sec:BioFVM_options">8.2.2.1</a>) prior to initializing the microenvironment, or at later times using the function</p>
<p><strong><code>void Microenvironment::set_substrate_dirichlet_activation( int substrate_index , bool new_value )</code></strong> This function sets the substrate at index <code>substrate_index</code> to have/not have a Dirichlet condition based on the <code>true</code>/<code>false</code> value of <code>new_value</code>. This activation vector is applied to <em>all</em> voxels.</p>
<p><strong><code>bool Microenvironment::get_substrate_dirichlet_activation( int substrate_index )</code></strong> This function returns the default enabled/disabled state of Dirichlet conditions for substrate with index <code>substrate_index</code>. Note that if any particular voxel is not a Dirichlet node, then this value is not relevant.</p>
<p><strong><code>void Microenvironment::set_substrate_dirichlet_activation( int substrate_index , int index, bool new_value )</code></strong> This function sets the substrate at index <code>substrate_index</code> in voxel <code>index</code> to have/not have a Dirichlet condition based on the <code>true</code>/<code>false</code> value of <code>new_value</code>.</p>
<p><strong><code>bool Microenvironment::get_substrate_dirichlet_activation( int substrate_index , int index )</code></strong> This function returns the enabled/disabled state of Dirichlet conditions for substrate with index <code>substrate_index</code> in voxel <code>index</code>.</p>
<p>For example:</p>
<pre><code>\\ set options for the substrate with index 2 to false 

default_microenvironment_options.Dirichlet_activation_vector[2] = false; 

\\ initialize the microenvironment with the currently set options 

initialize_microenvironment(); 

\\ set the Dirichlet conditions in substrate 1 to true. 

get_default_microenvironment()-&gt;set_substrate_dirichlet_activation(1,true); </code></pre>
<p>Note that turning on or off a Dirichlet condition for a substrate applies it at all Dirichlet nodes for which <code>is_dirichlet_node(int voxel_index)</code> is <code>true</code>.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:BioFVM_initial_conditions">Setting the initial conditions</h2>
<p>As of PhysiCell Version 1.5.0, users can use <code>default_microenvironment_options.initial_condition_vector</code> to set the initial conditions for all substrates (uniformly) across the mesh. For example, suppose we have substrates oxygen (units: mmHg) and glucose (dimensionless), and we want to use the initial conditions (38, 0.83). We would insert this code within the <code>setup_microenvironment()</code> function, and prior to calling <code>initialize_microenvironment()</code>:</p>
<pre><code>void setup_microenvironment( void )
{
   // no gradients need for this example 
   default_microenvironment_options.calculate_gradients = false; 
    
   // set Dirichlet conditions 
   default_microenvironment_options.outer_Dirichlet_conditions = true;
    
   // if there are more substrates, resize accordingly 
   std::vector&lt;double&gt; bc_vector.Dirichlet_condition_vector = { 40.0, 1.0 };
        
   // set initial conditions 
   default_microenvironment_options.initial_condition_vector = { 38.0 , 0.83 }; 
    
   // initialize BioFVM 
   initialize_microenvironment();   
    
   return; 
}</code></pre>
<p>Note that users have not set <code>default_microenvironment_options.initial_condition_vector</code> prior to calling <code>initialize_microenvironment()</code>, then BioFVM / PhysiCell reverts to its prior behavior: it uses <code>default_microenvironment_options.Dirichlet_condition_vector</code> as a sensible default for initial conditions.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:BioFVM_nonuniform_initial_condition">Setting a non-uniform initial condition</h3>
<p>Users may want a non-uniform initial condition. This can be accopmlished by cycling through all voxels and setting the substrate values. This must be performed after <code>initialize_microenvironment()</code> to avoid being overwritten by the built-in behavior. For example, to set the initial oxygen to <span class="math inline">$e^{-\frac{x}{100}}$</span>, use code like this:</p>
<pre><code>void setup_microenvironment( void )
{
   // no gradients need for this example 
   default_microenvironment_options.calculate_gradients = false; 
    
   // set Dirichlet conditions 
   default_microenvironment_options.outer_Dirichlet_conditions = true;
    
   // if there are more substrates, resize accordingly 
   std::vector&lt;double&gt; bc_vector.Dirichlet_condition_vector = { 40.0, 1.0 };
        
   // set initial conditions 
   default_microenvironment_options.initial_condition_vector = { 38.0 , 0.83 }; 
    
   // initialize BioFVM 
   initialize_microenvironment();   
   
   // set a new initial condition for oxygen
   int k = microenvironment.find_density_index( &quot;oxygen&quot; ); // find its index 
   for( int n=0; n &lt; microenvironment.number_of_voxels(); n++ )
   {
    // x coordinate of the nth voxel&#39;s center  
    x = microenvironment.mesh.voxels[n].center[0]; 
    // access kth substrate of the nth voxel 
    microenvironment(n)[k] = exp( -x / 100.0 ); 
   }
    
   return; 
}</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:BioFVM_internalization_tracking">Automated tracking of internalized substrates</h2>
<p>As of PhysiCell 1.5.0, each individual <code>Basic_Agent</code> can track the net total amount of substrates uptaken and secreted over its lifetime, conserving mass with the uptake/secretion/export terms in the governing PDEs in <span class="citation" data-cites="ref:BioFVM"></span>. By matching to system of PDEs in BioFVM (with the Dirac delta function approximation used in the code), in any time step <span class="math inline"><em>Δ</em><em>t</em></span>, the total amount of net mass transferred from the <span class="math inline"><em>i</em><sup><em>t</em><em>h</em></sup></span> cell (sitting in voxel <span class="math inline"><em>Ω</em><sub><em>n</em></sub></span>) into the microenvironment is given by: <span class="math display">$$\begin{aligned}
\Delta t \int_{\Omega_n} \boldsymbol{\rho} \: dV 
&amp; = &amp; \Delta t \int_{\Omega_n }  \delta( \mathbf{x} - \mathbf{x}_i ) 
\Bigl( V_i \mathbf{S}_i \circ 
\left( \boldsymbol{\rho}^*_i - \boldsymbol{\rho} \right) - V_i \mathbf{U}_i \circ \boldsymbol{\rho} + \mathbf{E}_i \Bigr) dV 
\nonumber \\
&amp; = &amp; 
\Delta t 
\Bigl( V_i \mathbf{S}_i \circ 
\left( \boldsymbol{\rho}^*_i - \boldsymbol{\rho}(\mathbf{x}_n) \right) - V_i \mathbf{U}_i \circ \boldsymbol{\rho}(\mathbf{x}_n) + \mathbf{E}_i \Bigr)   \end{aligned}$$</span> After comparing against the numerical implementation in BioFVM to calculate <span class="math inline"><em>Δ</em><strong>ρ</strong></span>, and multiplying this by the volume of the voxel, we get that the net total change in external substrates between <span class="math inline"><em>t</em></span> and <span class="math inline"><em>t</em> + <em>Δ</em><em>t</em></span> is <span class="math display">$$\Delta \mathbf{n}_k = W_k 
\left( \frac{(\boldsymbol{1}-\mathbf{c}_2) \circ \boldsymbol{\rho}_k + \mathbf{c}_1 }{ \mathbf{c}_2 } \right) + \mathbf{E}_i , 
% \left( \frac{ (1-\vec{c}_2) \grvec{\rho}_k + \vec{c}_1} }{ \vec{c}_2 } \right),$$</span> where <span class="math inline"><em>W</em><sub><em>k</em></sub></span> is the volume of the voxel, <span class="math inline"><strong>c</strong><sub><em>i</em></sub></span> are internal constants already calculated for the BioFVM secretion/uptake functions, and division of vectors is element-wise. For conservation of mass, the net change in the cell’s internalized substrates is <span class="math display">$$-W_k 
\left( \frac{(\boldsymbol{1}-\mathbf{c}_2) \circ \boldsymbol{\rho}_k + \mathbf{c}_1 }{ \mathbf{c}_2 } \right) - \mathbf{E}_i, 
% \left( \frac{ (1-\vec{c}_2) \grvec{\rho}_k + \vec{c}_1} }{ \vec{c}_2 } \right),$$</span> If <code>default_microenvironment_options.track_internalized_substrates_in_each_agent = true</code>, then PhysiCell will automatically perform these calculations in every cell at every diffusion time step.</p>
<p>Note that users should <em>access</em> these internalized substrates via the <code>molecular</code> part of the cell’s <code>phenotype</code>. See Section <a href="#sec:phenotype_molecular" data-reference-type="ref" data-reference="sec:phenotype_molecular">11.8</a>.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:BioFVM_auto_release_at_death">Automated release of internalized substrates at cell death</h3>
<p>Users can optionally set PhysiCell to release some or all of its internalized substrates at the end of cell death or at lysis. This functionality is accessed through the <code>Molecular</code> portion of the <code>Phenotype</code>. See Section <a href="#sec:phenotype_molecular" data-reference-type="ref" data-reference="sec:phenotype_molecular">11.8</a>.</p>
<hr />
</div>
<h2 id="sec:BioFVM_further_reading">Other BioFVM resources</h2>
<p>To learn more about using BioFVM, take a look at the tutorials at:</p>
<p><a href="http://mathcancer.org/blog/biofvm-tutorials/">http://mathcancer.org/blog/biofvm-tutorials/</a></p>
<hr />
</div>
<h1 id="sec:Cells">Cells </h1>
<p>Each <code>Cell</code> is an extension of BioFVM’s <code>Basic_Agent</code> class. As such, it has access to all the parent class’s member data and functions. In PhysiCell, Cells have the following major parts:</p>
<ol>
<li><p><strong><code>std::string type_name:</code></strong> The name of the type of cell.</p></li>
<li><p><strong><code>Custom_Cell_Data custom_data:</code></strong> Custom data attached the cell, which may differ from other cells. See Section <a href="#sec:Custom_Cell_Data" data-reference-type="ref" data-reference="sec:Custom_Cell_Data">9.4.1</a>.</p></li>
<li><p><strong><code>Cell_Parameters parameters:</code></strong> A set of standardized parameters (which may eventually be moved into the cell’s phenotype). See Section <a href="#sec:Cell_Parameters" data-reference-type="ref" data-reference="sec:Cell_Parameters">9.4.2</a>.</p></li>
<li><p><strong><code>Cell_Functions functions:</code></strong> A collection of functions used for updating the cell phenotype, including custom functions. See Section <a href="#sec:Cell_Functions" data-reference-type="ref" data-reference="sec:Cell_Functions">9.4.3</a>.</p></li>
<li><p><strong><code>Cell_State cell_state:</code></strong> A small set of standard state variables, chiefly (basal-to-apical) orientation. See Section <a href="#sec:Cell_State" data-reference-type="ref" data-reference="sec:Cell_State">9.4.4</a>.</p></li>
<li><p><strong><code>Phenotype phenotype:</code></strong> A hierarchical organization of the cell’s properties. This data element is discussed in great depth in Section <a href="#sec:Phenotype" data-reference-type="ref" data-reference="sec:Phenotype">10</a>.</p></li>
</ol>
<p>The following inherited member data and functions (from <code>Basic_Agent</code>) are especially helpful:</p>
<ol>
<li><p><strong><code>int ID</code></strong> is a unique integer identifier for the cell. No other cell now or in the future will have the same <code>ID</code>.</p></li>
<li><p><strong><code>int index</code></strong> is the cell’s current index in <code>std::vector&lt;Basic_Agent*&gt; all_basic_agents</code>, the list of all current <code>Basic_Agents</code> in the simulation.</p></li>
<li><p><strong><code>int type</code></strong> is a user-specified (default 0) integer code to classify the cell’s type. Use these to quickly compare if two cells are of the same or different types, or to perform type-specific operations on them.</p></li>
<li><p><strong><code>int get_current_voxel_index( void )</code></strong> returns the cell’s positional index in the BioFVM Microenvironment.</p></li>
<li><p><strong><code>std::vector&lt;double&gt;&amp; nearest_density_vector( void )</code></strong> allows the user to directly access (i.e., sample or modify) the vector of substrates at the cell’s position. This is useful building functions that alter cell phenotype based on the microenvironment.</p></li>
<li><p><strong><code>std::vector&lt;double&gt;&amp; nearest_gradient( int substrate_index )</code></strong> returns (by reference) the gradient of the substrate with index <code>substrate_index</code>, at the cell’s current position. This is useful for things like chemotaxis.</p></li>
<li><p><strong><code>std::vector&lt;gradient&gt;&amp; nearest_gradient_vector( void )</code></strong> returns a vector of <em>all</em> the substrate gradients at the cell’s position. Each <code>gradient</code> is a <code>std::vector&lt;double&gt;</code> of size 3.</p></li>
<li><p><strong><code>void release_internalized_substrates( void )</code></strong> immediately releases none / some / all internalized substrates to the cell’s position in extracellular space, according to the release fraction specified in the phenotype. It sets all internalized substrate levels to zero thereafter. This function is automatically called when a cell is about to be removed from the simulation, as long as internalized substrate tracking is enabled. See Sections <a href="#sec:BioFVM_internalization_tracking" data-reference-type="ref" data-reference="sec:BioFVM_internalization_tracking">8.6</a>, <a href="#sec:BioFVM_auto_release_at_death" data-reference-type="ref" data-reference="sec:BioFVM_auto_release_at_death">8.6.1</a>, and <a href="#sec:phenotype_molecular" data-reference-type="ref" data-reference="sec:phenotype_molecular">11.8</a>. (Introduced in 1.5.2.)</p></li>
</ol>
<p>Here is how the <code>Cell</code> class is defined in <code>PhysiCell_cell.h</code>:</p>
<pre><code>class Cell : public Basic_Agent 
{
 private: 
    Cell_Container * container;
    int current_mechanics_voxel_index;
    int updated_current_mechanics_voxel_index; 
 public:
    std::string type_name; 
 
    Custom_Cell_Data custom_data;
    Cell_Parameters parameters;
    Cell_Functions functions; 
    
    Cell_State state; 
    Phenotype phenotype; 
    
    void update_motility_vector( double dt_ );
    void advance_bundled_phenotype_functions( double dt_ ); 
    
    void add_potentials(Cell*);
    void set_previous_velocity(double xV, double yV, double zV);
    int get_current_mechanics_voxel_index();
    void turn_off_reactions(double);  
    
    bool is_out_of_domain;
    bool is_movable;
    
    void flag_for_division( void );   
    void flag_for_removal( void );   
    
    void start_death( int death_model_index ); 
    void lyse_cell( void ); 

    Cell* divide( void );
    void die( void );
    void step(double dt);
    Cell();
    
    bool assign_position(std::vector&lt;double&gt; new_position);
    bool assign_position(double, double, double);
    void set_total_volume(double);
    void set_radius(double); 
    
    void set_target_volume(double); 
    void set_target_radius(double); 
    
    double&amp; get_total_volume(void);
    
    // mechanics 
    void update_position( double dt );  
    std::vector&lt;double&gt; displacement; 

    void assign_orientation();  
    
    void copy_function_pointers(Cell*);
    
    void update_voxel_in_container(void);
    void copy_data(Cell *);
    
    void ingest_cell( Cell* pCell_to_eat );     

    void set_phenotype( Phenotype&amp; phenotype );  
    void update_radius();
    Cell_Container * get_container();
    
    std::vector&lt;Cell*&gt;&amp; cells_in_my_container( void ); 
    
    void Cell::convert_to_cell_definition( Cell_Definition&amp; cd )
};</code></pre>

<h2 id="sec:cell_other_member_data">Other member data</h2>
<ol>
<li><p><strong><code>bool is_out_of_domain</code></strong> is <code>true</code> if the cell is out of the simulation domain boundaries.</p></li>
<li><p><strong><code>bool is_movable</code></strong> indicates whether the cell is in a static position. Set this to <code>true</code> if you would like PhysiCell to leave its position fixed and not evaluate the mechanics models for this cell. Note that it can still exert adhesive and repulsive forces on other cells.</p></li>
</ol>
<h2 id="sec:cell_member_functions">Member functions</h2>
<ol>
<li><p><strong><code>void update_motility_vector( double dt_ )</code></strong> updates the cell’s motility vector, based on the following model:</p>
<p>First, check if the cell should change its direction of motility <span class="math inline"><strong>v</strong><sub><em>m</em><em>o</em><em>t</em></sub></span> within the next <span class="math inline"><em>Δ</em><em>t</em></span> time:</p>
<ol>
<li><p>If <code>is_motile == false</code> set <span class="math inline"><strong>v</strong><sub><em>m</em><em>o</em><em>t</em></sub> = <strong>0</strong></span> and exit.</p></li>
<li><p>Let <span class="math inline"><em>s</em> ∈ <em>U</em>(0, 1)</span> be a random number from the uniform distribution on <span class="math inline">[0, 1]</span>.</p></li>
<li><p>If <span class="math inline"><em>s</em> ≤ <em>Δ</em><em>t</em>/<em>T</em><sub><em>p</em><em>e</em><em>r</em></sub></span> or if <span class="math inline"><em>Δ</em><em>t</em> &lt; <em>T</em><sub><em>p</em><em>e</em><em>r</em></sub></span> (where <span class="math inline"><em>T</em><sub><em>p</em><em>e</em><em>r</em></sub></span> is the cell’s mean persistence time), then continue. Otherwise, leave <span class="math inline"><strong>v</strong><sub><em>m</em><em>o</em><em>t</em></sub></span> unchanged and exit.</p></li>
<li><p>Choose a random direction <span class="math inline"><strong>ξ</strong></span> in 3-D:</p>
<ol>
<li><p>Choose <span class="math inline"><em>θ</em> ∈ <em>U</em>(0, 2<em>π</em>)</span> to be a random angle in <span class="math inline">[0, 2<em>π</em>]</span>.</p></li>
<li><p>Choose <span class="math inline"><em>ϕ</em> ∈ <em>U</em>(0, <em>π</em>)</span> to be a random angle in <span class="math inline">[0, <em>π</em>]</span>. If <code>restrict_to_2D == true</code>, set <span class="math inline">$\phi = \frac{\pi}{2}$</span>.</p></li>
<li><p>Set <span class="math inline"><strong>ξ</strong> = [sin(<em>ϕ</em>)cos(<em>θ</em>),sin(<em>ϕ</em>)sin(<em>θ</em>),cos(<em>ϕ</em>)]</span>.</p></li>
</ol></li>
<li><p>Update the motility bias vector <span class="math inline"><strong>b</strong></span> and the bias <span class="math inline"><em>b</em></span> by calling <code>functions.update_migration_bias</code>.</p></li>
<li><p>Set <span class="math inline"><strong>v</strong><sub><em>m</em><em>o</em><em>t</em></sub></span> according to biased random motion: <span class="math display">$$\mathbf{v}_\mathrm{mot} 
= 
s_\mathrm{mot} 
\frac{ 
( 1 - b) \boldsymbol{\xi} + b \mathbf{b} 
} 
{ 
\left|\left|{ ( 1 - b) \boldsymbol{\xi} + b \mathbf{b}  }\right|\right|
}$$</span> Here <span class="math inline">0 ≤ <em>b</em> ≤ 1</span> is the motility bias (<code>phenotype.motility.migration_bias</code>), <span class="math inline"><strong>b</strong></span> is the migration bias direction (<code>phenotype.motility.migration_bias_direction</code>), and <span class="math inline"><em>s</em><sub><em>m</em><em>o</em><em>t</em></sub></span> is the migration speed (<code>phenotype.motility.migration_speed</code>). See Section <a href="#sec:Motility" data-reference-type="ref" data-reference="sec:Motility">11.6</a>.</p></li>
</ol>
<p>See Section <a href="#sec:Cell_Functions" data-reference-type="ref" data-reference="sec:Cell_Functions">9.4.3</a> for more information on cell functions, and Section <a href="#sec:Motility" data-reference-type="ref" data-reference="sec:Motility">11.6</a> for further details on cell motility.</p></li>
<li><p><strong><code>void advance_bundled_phenotype_functions( double dt_ )</code></strong> automatically runs the following cell functions once every phenotype time step (by default, once per 6 simulated minutes):</p>
<ol>
<li><p>Evaluate <code>functions.update_phenotype</code> to update the phenotype based upon the current sampling of the microenvironment and any other parameters (e.g., cell-cell interactions). If <code>update_phenotype == NULL</code>, this is skipped. See Section <a href="#sec:Phenotype" data-reference-type="ref" data-reference="sec:Phenotype">10</a> for more information on the cell phenotype class.</p></li>
<li><p>Advance the cell volume model by <code>dt_</code> time by calling <code>functions.volume_update_function</code>. Skip this step if <code>functions.volume_update_function == NULL</code>. See Section <a href="#sec:Volume" data-reference-type="ref" data-reference="sec:Volume">11.3</a> for more information on cell volume.</p></li>
<li><p>Update the cell geometry (radius, nuclear radius, surface area, etc.) by calling <code>phenotype.geometry.update</code>. See Section <a href="#sec:Geometry" data-reference-type="ref" data-reference="sec:Geometry">11.4</a> for more information on the cell geometry.</p></li>
<li><p>Check for death events in the next <code>dt_</code> time (such as apoptosis and necrosis) by calling <code>phenotype.death.check_for_death</code>. If the function returns <code>true</code>, set the cell’s current cycle model to the appropriate death model, evaluate any death entry functions, and set motility to zero. Cell secretions are set to zero, and cell uptake is cut by a factor of 10. (Users can make further changes to secretion/export and uptake using <code>entry_function</code>s that are called at the start of a death model phase. See Section <a href="#sec:Phase" data-reference-type="ref" data-reference="sec:Phase">11.1.1</a>.) See Section <a href="#sec:Death" data-reference-type="ref" data-reference="sec:Death">11.2</a> for more information on cell death, and see Section <a href="#sec:Cycle" data-reference-type="ref" data-reference="sec:Cycle">11.1</a> on the general cycle class.</p></li>
<li><p>Advance the current cycle model, whether it is a (live) cell cycle model or a death cycle model, by calling <code>phenotype.cycle.advance_cycle</code>. See Section <a href="#sec:Cycle" data-reference-type="ref" data-reference="sec:Cycle">11.1</a> for more details.</p></li>
<li><p>If <code>phenotype.flagged_for_removal == true</code>, call <code>flag_for_removal()</code>. If <code>phenotype.flagged_for_division == true</code>, call <code>flag_for_division()</code>.</p></li>
</ol>
<p>See Section <a href="#sec:Cell_Functions" data-reference-type="ref" data-reference="sec:Cell_Functions">9.4.3</a> for more details on these cell functions, and Section <a href="#sec:Examples" data-reference-type="ref" data-reference="sec:Examples">19</a> for examples.</p></li>
<li><p><strong><code>void add_potentials(Cell*)</code></strong> is used in the mechanics functions. Users should almost never call this function.</p></li>
<li><p><strong><code>void set_previous_velocity(double xV, double yV, double zV)</code></strong> sets the cell’s previous velocity (for use in Adams-Bashforth evolution of the cell position) to <code>[xV,yV,zV]</code>. Users are not expected to ever need to call this function.</p></li>
<li><p><strong><code>int get_current_mechanics_voxel_index()</code></strong> returns the index of the <code>Container</code> currently containing the cell.</p></li>
<li><p><strong><code>void turn_off_reactions(double)</code></strong> turns off all secretions/exports and uptake by the cell.</p></li>
<li><p><strong><code>void flag_for_division( void )</code></strong> adds the cell to the list of cells that should divide at the next opportunity.</p></li>
<li><p><strong><code>void flag_for_removal( void )</code></strong> adds the cell to the list of cells that should be removed from the simulation at the next opportunity.</p></li>
<li><p><strong><code>void start_death( int death_model_index )</code></strong> immediately kills the cell (with the death model indicated by <code>death_model_index</code>), sets <code>cell.phenotype.death.dead = true</code>, sets motility to zero, sets secretion to zero, cuts all uptake by a factor of ten, and executes any “entry” functions for the associated death model. Note that this function does not by default set all the cell’s custom functions to <code>NULL</code>.</p>
<p><span style="color: red">This is the preffered method to trigger death in a cell.</span></p></li>
<li><p><strong><code>void lyse_cell( void )</code></strong> triggers immediate degradation and removal of the cell. If already enabled, none, some, or all of the cell’s internalized substrates will be released to the microenvironment, as set in <code>phenotype.molecular.fraction_released_at_death</code>. See Section <a href="#sec:phenotype_molecular" data-reference-type="ref" data-reference="sec:phenotype_molecular">11.8</a>.</p></li>
<li><p><strong><code>Cell* divide( void )</code></strong> performs cell division, and returns the memory address of the newly-created cell.</p></li>
<li><p><strong><code>void die( void )</code></strong> removes the cell from the simulation.</p></li>
<li><p><strong><code>void step(double dt)</code></strong> is neither used nor implemented. It will be deprecated.</p></li>
<li><p><strong><code>Cell()</code></strong> is the default constructor. Users should use the <code>create_cell</code> functions rather than this constructor. See Section <a href="#sec:other_key_cell_functions" data-reference-type="ref" data-reference="sec:other_key_cell_functions">9.3</a>.</p></li>
<li><p><strong><code>bool assign_position(std::vector&lt;double&gt; new_position)</code></strong> safely sets the cell’s position to <code>new_position</code>. Always use this rather than directly editing <code>position</code> (inherited from <code>Basic_Agent</code>).</p></li>
<li><p><strong><code>bool assign_position(double, double, double)</code></strong> performs the same function as above, but supplying the x, y, and z coordinates separately.</p></li>
<li><p><strong><code>void set_total_volume(double)</code></strong> safely sets the cell’s total volume. It also sets the cell’s sub-volumes proportionally. Note that this does not change the <em>target</em> value, so the cell will still grow or shrink towards its (unaltered) targets.</p></li>
<li><p><strong><code>void set_radius(double)</code></strong> safely sets the cell’s radius (by calling <code>set_total_volume(double)</code>. Note that this does not change the <em>target</em> value, so the cell will still grow or shrink towards its (unaltered) targets.</p></li>
<li><p><strong><code>void set_target_volume(double)</code></strong> safely sets the cell’s total target volume. It also sets the cell’s sub-volumes proportionally. Note that this does not change the <em>current</em> value, so the cell needs to shrink or grow towards this new target.</p></li>
<li><p><strong><code>void set_radius(double)</code></strong> safely sets the cell’s total target radius. It also sets the cell’s sub-volumes proportionally. Note that this does not change the <em>current</em> value, so the cell need to shrink or grow towards this new target.</p></li>
<li><p><strong><code>double&amp; get_total_volume(void)</code></strong> returns the cell’s current total volume, stored in<br />
<code>cell.phenotype.volume.total</code>. It is <em>not</em> the preferred way to access this data, but it is provided to overwrite the base <code>Basic_Agent::get_total_volume</code> function.</p></li>
<li><p><strong><code>void update_position( double dt )</code></strong> uses the cell’s current and previous velocities to safely update the cell’s position, using the second-order Adams-Bashforth algorithm.</p></li>
<li><p><strong><code>void assign_orientation()</code></strong> sets the cell’s <code>state.orientation</code> according to its current model (if any). See Section <a href="#sec:Cell_Functions" data-reference-type="ref" data-reference="sec:Cell_Functions">9.4.3</a>.</p></li>
<li><p><strong><code>void copy_function_pointers(Cell*)</code></strong> overwrites the functions in <code>functions</code> with those from the supplied <code>Cell</code>.</p></li>
<li><p><strong><code>void update_voxel_in_container(void)</code></strong> updates the cell’s position within the interaction testing data structure.</p></li>
<li><p><strong><code>void copy_data(Cell *)</code></strong> copies the member data (including <code>custom_data</code>, <code>parameters</code>, but <em>not</em> <code>phenotype</code> from the Cell at <code>Cell*</code>.</p></li>
<li><p><strong><code>void ingest_cell( Cell* pCell_to_eat )</code></strong> allows a cell to ingest (e.g., phagocytose) a cell. When this happens, the cell gains:</p>
<ol>
<li><p>all of the cell’s fluid volume;</p></li>
<li><p>all of the cell’s nuclear solid and cytoplasmic solid volume (which are added to the nuclear cytoplasmic solid volume);</p></li>
<li><p>none, some, or all of the cell’s internalized substrates, as set in <code>pCell_to_eat-&gt;phenotype.molecular.fraction_transferred_when_ingested</code>. See Section <a href="#sec:phenotype_molecular" data-reference-type="ref" data-reference="sec:phenotype_molecular">11.8</a>.</p></li>
</ol></li>
<li><p><strong><code>void set_phenotype( Phenotype&amp; phenotype )</code></strong> is no longer used and will be deprecated. Users can now safely overwrite the cell’s phenotype at any time.</p></li>
<li><p><strong><code>void update_radius()</code></strong> is neither implemented nor used. It will be deprecated.</p></li>
<li><p><strong><code>Cell_Container* get_container()</code></strong> returns the memory address of the <code>Cell_Container</code> containing the cell.</p></li>
<li><p><strong><code>std::vector&lt;Cell*&gt;&amp; cells_in_my_container( void )</code></strong> returns (by reference) a vector of pointers to the cells in the current mechanics voxel. <span style="color: red"><strong><em>For performance reasons, we are giving users direct access to the underlying data structures, rather than copies. It is critical that users do not alter the underlying array of <code>Cell*</code>.</em></strong></span> Future releases of PhysiCell will provide more refined access functions, including better lists of neighbors and lists of nearby mechanics voxels.</p></li>
<li><p><strong><code>void convert_to_cell_definition( Cell_Definition&amp; cd )</code></strong> converts the cell to match the name, type, custom data, parameters, function, and phenotype stored in the Cell Definition in <code>cd</code>. (See Section <a href="#sec:Cell_Definition" data-reference-type="ref" data-reference="sec:Cell_Definition">9.4.5</a> for more information on cell definitions.) As of Version 1.2.2, this function does not overwrite the <code>is_movable</code>, <code>is_out_of_domain</code>, and <code>displacement</code> data of the cell.</p>
<p>This function is particularly useful if you want to do looks like stem cell hierarchies, where you might “convert” a stem cell to a differentiated cell, each of which has been defined separately.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:other_key_cell_functions">Other key functions</h2>
<p>The following are functions in the <code>PhysiCell</code> namespace (and are not members of the <code>Cell</code> class).</p>
<ol>
<li><p><strong><code>Cell* create_cell( void )</code></strong> creates a new cell (with default <code>Cell_Definition</code>; see Section <a href="#sec:Cell_Definition" data-reference-type="ref" data-reference="sec:Cell_Definition">9.4.5</a>) at (0,0,0) and registers it in all the relevant data structures. This is the <em>safe</em> way to create a new cell in the simulation.</p>
<p><u>Example:</u> Let’s create a cell (with the default <code>Cell_Definition</code>) at (15,27,-32):</p>
<pre><code>Cell* pC = create_cell(); 
pC-&gt;assign_position(15,27,-32);</code></pre></li>
<li><p><strong><code>Cell* create_cell( Cell_Definition&amp; cd )</code></strong> creates a new cell at (0,0,0) with parameters, phenotype, functions, and other properties specified in <code>cd</code> (See Section <a href="#sec:Cell_Definition" data-reference-type="ref" data-reference="sec:Cell_Definition">9.4.5</a>), and registers it in all the relevant data structures. This is the <em>safe</em> way to create a new cell in the simulation.</p>
<p><u>Example:</u> Let’s define a new type of cell (<code>stem_cell</code>), then create a new cell of this type at (15,27,-32):</p>
<pre><code>// create a new cell definition 
Cell_Definition stem_cell; 

// Operations to set the properties and models 
// of the stem_cell type go here. 

// create a new stem_cell, and move it. 
Cell* pC = create_cell(stem_cell); 
pC-&gt;assign_position(15,27,-32);</code></pre></li>
<li><p><strong><code>void delete_cell( int )</code></strong> deletes the cell located at <code>all_cells(int)</code> and removes it from all relevant data structures. This is the <em>safe</em> way to directly remove a cell from a simulation.</p>
<p><u>Example:</u> Let’s check the 13th cell and delete it if a custom variable “infected” (See Section <a href="#sec:Custom_Cell_Data" data-reference-type="ref" data-reference="sec:Custom_Cell_Data">9.4.1</a>) indicates that it is infected. (See Section <a href="#sec:All_Cells" data-reference-type="ref" data-reference="sec:All_Cells">16.4</a> for more on the vector <code>all_cells</code> that lists the memory addresses of all cells.)</p>
<pre><code>Cell* pCell = (*all_cells)[13]; 

if( pCell-&gt;custom_data[ &quot;infected&quot; ] == true )
{
    delete_cell( 13 ); 
}</code></pre></li>
<li><p><strong><code>void delete_cell( Cell* )</code></strong> deletes the cell with located at <code>Cell*</code> and removes it from all relevant data structures. This is the <em>safe</em> way to directly remove a cell from a simulation.</p>
<p><u>Example:</u> Let’s check the 13th cell and delete it if a custom variable “infected” (See Section <a href="#sec:Custom_Cell_Data" data-reference-type="ref" data-reference="sec:Custom_Cell_Data">9.4.1</a>) indicates that it is infected. (See Section <a href="#sec:All_Cells" data-reference-type="ref" data-reference="sec:All_Cells">16.4</a> for more on the vector <code>all_cells</code> that lists the memory addresses of all cells.)</p>
<pre><code>Cell* pCell = (*all_cells)[13]; 

if( pCell-&gt;custom_data[ &quot;infected&quot; ] == true )
{
    delete_cell( pCell ); 
}</code></pre></li>
<li><p><strong><code>void display_cell_definitions( std::ostream&amp; os )</code></strong> does a basic display of all cell definitions, including basic information on which cell cycle and death models are included, custom functions, and custom data.</p>
<p><u>Example:</u></p>
<pre><code>display_cell_definitions( std::cout ); </code></pre></li>
<li><p><strong><code>void build_cell_definitions_maps( void )</code></strong> builds the internal registries of all cell definitions, which can be searched by name or type (integer code). This is vest to use at the end of <code>setup_tissue()</code>.</p></li>
<li><p><strong><code>Cell_Definition* find_cell_definition( std::string search_string )</code></strong> returns a pointer to the cell definition with name as searched. If none is found, it returns <code>NULL</code>.</p>
<p><u>example:</u> Let’s find the tumor cell definition and display its default apoptosis rate.</p>
<pre><code>Cell_Definition* pCD = find_cell_definition( &quot;tumor&quot; ); 
std::cout &lt;&lt; &quot;Default apoptotic death rate: &quot;; 
int apop_index = pCD-&gt;phenotype.death.find_death_model_index( &quot;apoptosis&quot; ); 
std::cout &lt;&lt; pCD-&gt;phenotype.death.rates[ apop_index ] &lt;&lt; std::endl; </code></pre>
<p><strong><code>Cell_Definition* find_cell_definition( int search_type )</code></strong> Let’s find the tumor cell definition with type 3 and display its name and default apoptosis rate.</p>
<pre><code>Cell_Definition* pCD = find_cell_definition( 3 ); 
std::cout &lt;&lt; &quot;Cell type name for type 3: &quot; &lt;&lt; pCD-&gt;name &lt;&lt; std::endl; 
std::cout &lt;&lt; &quot;Default apoptotic death rate: &quot;; 
int apop_index = pCD-&gt;phenotype.death.find_death_model_index( &quot;apoptosis&quot; ); 
std::cout &lt;&lt; pCD-&gt;phenotype.death.rates[ apop_index ] &lt;&lt; std::endl; </code></pre></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="important-classes-except-phenotype">Important classes (except Phenotype)</h2>
<h3 id="sec:Custom_Cell_Data">Custom_Cell_Data</h3>
<p>This class allows users to dynamically add new custom data to individual cells, or to a <code>Cell_Definition</code>. (See Section <a href="#sec:Cell_Definition" data-reference-type="ref" data-reference="sec:Cell_Definition">9.4.5</a>.) Here is the full class definition:</p>
<pre><code>class Custom_Cell_Data
{
 private:
    std::unordered_map&lt;std::string,int&gt; name_to_index_map; 
    friend std::ostream&amp; operator&lt;&lt;(std::ostream&amp; os, const Custom_Cell_Data&amp; ccd);   
 public:
    std::vector&lt;Variable&gt; variables; 
    std::vector&lt;Vector_Variable&gt; vector_variables; 
    
    int add_variable( Variable&amp; v );   
    int add_variable( std::string name , std::string units , double value );   
    int add_variable( std::string name , double value );   

    int add_vector_variable( Vector_Variable&amp; v );   
    int add_vector_variable( std::string name , 
        std::string units , std::vector&lt;double&gt;&amp; value );   
    int add_vector_variable( std::string name , std::vector&lt;double&gt;&amp; value );   

    int find_variable_index( std::string name );   

    double&amp; operator[]( int i );  
    double&amp; operator[]( std::string name );   
    
    Custom_Cell_Data();   
    Custom_Cell_Data( const Custom_Cell_Data&amp; ccd ); 
};</code></pre>
<p>Here are the main data elements and member functions, in greater detail:</p>
<ol>
<li><p><strong><code>std::vector&lt;Variable&gt; variables</code></strong> is a vector of variables (initially empty). A <code>Variable</code> has the following form:</p>
<pre><code>class Variable
{
 private:
    friend std::ostream&amp; operator&lt;&lt;(std::ostream&amp; os, const Variable&amp; v);  
 public:
    std::string name; 
    double value; 
    std::string units; 
    
    Variable(); 
};</code></pre></li>
<li><p><strong><code>std::vector&lt;Vector_Variable&gt; vector_variables</code></strong> is a vector of vector variables (initially empty). A <code>Vector_Variable</code> has the following form:</p>
<pre><code>class Vector_Variable
{
 private:
    friend std::ostream&amp; operator&lt;&lt;(std::ostream&amp; os, const Vector_Variable&amp; v);   
    
 public:
    std::string name; 
    std::vector&lt;double&gt; value; 
    std::string units; 
    
    Vector_Variable(); 
};</code></pre></li>
<li><p><strong><code>int add_variable( Variable&amp; v )</code></strong> adds the new variable <code>v</code> to the custom data, and returns the index of the newly added variable.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 
Variable v; 

v.name = &quot;sensitivity&quot;; 
v.value = 0.3; 
v.units = &quot;dimensionless&quot;; 

ccc.add_variable( v ); </code></pre></li>
<li><p><strong><code>int add_variable( std::string name , std::string units , double value )</code></strong> adds a new variable with name <code>name</code>, units <code>units</code>, and value <code>value</code>. It returns the index of the newly added variable.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 
ccd.add_variable( &quot;sensitivity&quot;, &quot;dimensionless&quot;, 0.3 ); </code></pre></li>
<li><p><strong><code>int add_variable( std::string name , double value )</code></strong> adds a new variable with name <code>name</code>, unspecified units, and value <code>value</code>. It returns the index of the newly added variable.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 
ccd.add_variable( &quot;sensitivity&quot;, 0.3 ); </code></pre></li>
<li><p><strong><code>int add_vector_variable( Vector_Variable&amp; v )</code></strong> adds the new vector variable <code>v</code> to the custom data, and returns the index of the newly added variable.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 
Vector_Variable v; 

v.name = &quot;home&quot;; 
v.value = {0,1,2}; 
v.units = &quot;micron&quot;; 

ccc.add_vector_variable( v ); </code></pre></li>
<li><p><strong><code>int add_vector_variable( std::string name, std::string units, std::vector&lt;double&gt;&amp; value )</code></strong> adds a new vector variable with name <code>name</code>, units <code>units</code>, and (vector) value <code>value</code>. It returns the index of the newly added variable.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 

std::vector&lt;double&gt; myvec = {0,1,2}; 

ccc.add_vector_variable( &quot;home&quot;, &quot;micron&quot;, myvec ); </code></pre></li>
<li><p><strong><code>int add_vector_variable( std::string name , std::vector&lt;double&gt;&amp; value )</code></strong> adds a new vector variable with name <code>name</code>, unspecified units, and (vector) value <code>value</code>. It returns the index of the newly added variable.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 

std::vector&lt;double&gt; myvec = {0,1,2}; 

ccc.add_vector_variable( &quot;home&quot;, myvec ); </code></pre></li>
<li><p><strong><code>int find_variable_index( std::string name )</code></strong> returns the index of the variable with name <code>name</code>, if it exists. Note that this function is case sensitive.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 

ccd.add_variable( &quot;oxygen&quot; , &quot;mmHg&quot;, 38.0 ); 
ccd.add_variable( &quot;maple syrup&quot; , &quot;megayums&quot;, 1.2 ); 
ccd.add_variable( &quot;VEGF&quot;, &quot;dimensionless&quot;, 0.01 ); 

int syrup_index = ccd.find_variable_index( &quot;maple syrup&quot; ); 
std::cout &lt;&lt; ccd.variables[syrup_index].value &lt;&lt; std::endl; </code></pre></li>
<li><p><strong><code>double&amp; operator[]( int i )</code></strong> access the ith scalar variable.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 

ccd.add_variable( &quot;oxygen&quot; , &quot;mmHg&quot;, 38.0 ); 
ccd.add_variable( &quot;maple syrup&quot; , &quot;megayums&quot;, 1.2 ); 
ccd.add_variable( &quot;VEGF&quot;, &quot;dimensionless&quot;, 0.01 ); 

int syrup_index = ccd.find_variable_index( &quot;maple syrup&quot; ); 
std::cout &lt;&lt; ccd.variables[syrup_index].value &lt;&lt; std::endl; 
std::cout &lt;&lt; ccd[syrup_index] &lt;&lt; std::endl; </code></pre></li>
<li><p><strong><code>double&amp; operator[]( std::string name )</code></strong> access the scalar variable with name <code>name</code>. Note that this function is case sensitive.</p>
<p><u>Example:</u></p>
<pre><code>Custom_Cell_Data ccd; 

ccd.add_variable( &quot;oxygen&quot; , &quot;mmHg&quot;, 38.0 ); 
ccd.add_variable( &quot;maple syrup&quot; , &quot;megayums&quot;, 1.2 ); 
ccd.add_variable( &quot;VEGF&quot;, &quot;dimensionless&quot;, 0.01 ); 

int syrup_index = ccd.find_variable_index( &quot;maple syrup&quot; ); 
std::cout &lt;&lt; ccd.variables[syrup_index].value &lt;&lt; std::endl; 
std::cout &lt;&lt; ccd[syrup_index] &lt;&lt; std::endl; 
std::cout &lt;&lt; ccd[&quot;maple syrup&quot;] &lt;&lt; std::endl; </code></pre></li>
<li><p><strong><code>Custom_Cell_Data()</code></strong> is the default constructor. It creates a custom cell data structure with no variables and no vector variables.</p></li>
<li><p><strong><code>Custom_Cell_Data( const Custom_Cell_Data&amp; ccd )</code></strong> is the copy constructor, where the new <code>Custom_Cell_Data</code> is initialized with all contents equal to <code>ccd</code>.</p></li>
<li><p><strong>Streaming:</strong> You can display a custom variable to any <code>C++</code> streaming operator.</p>
<p><u>Example:</u> We’ll create a custom cell data structure called <code>my_custom_data</code>, add some scalar and vector variables, and display it.</p>
<pre><code>my_custom_data.add_variable( &quot;spring constant&quot;, &quot;1/min&quot; , 0.01 ); 
my_custom_data.add_variable( &quot;relaxation rate&quot;, &quot;1/min&quot; , 7e-5 ); 

my_custom_data.add_variable( &quot;strain&quot;, &quot;micron&quot; , 0.0 ); 
my_custom_data.add_variable( &quot;integrated strain&quot;, &quot;micron*min&quot; , 0.0 ); 

my_custom_data.add_variable( &quot;max strain&quot;, &quot;micron&quot; , 10.0 ); 
my_custom_data.add_variable( &quot;max integrated strain&quot;, &quot;micron*min&quot; , 600.0 ); 

my_custom_data.add_vector_variable( &quot;home&quot; , &quot;micron&quot; , {0,0,0} ); 

std::cout &lt;&lt; my_custom_data &lt;&lt; std::endl; </code></pre>
<p>The output should look like this:</p>
<pre><code>Custom data (scalar):
0: spring constant: 0.01 1/min
1: relaxation rate: 7.0e-005 1/min
2: strain: 0 micron
3: integrated strain: 0 micron*min
4: max strain: 10 micron
5: max integrated strain: 600 micron*min
Custom data (vector):
0: home: [0,0,0] micron </code></pre></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Cell_Parameters">Cell_Parameters</h3>
<p>This class stores standardized parameters for a <code>Cell</code> (or a <code>Cell_Definition</code>; see Section <a href="#sec:Cell_Definition" data-reference-type="ref" data-reference="sec:Cell_Definition">9.4.5</a>). In future editions of PhysiCell, some of these may be moved into the phenotype. (See Section <a href="#sec:Phenotype" data-reference-type="ref" data-reference="sec:Phenotype">10</a>.) Here is the full class definition:</p>
<pre><code>class Cell_Parameters
{
 private:
 public:
    double o2_hypoxic_threshold;  
    double o2_hypoxic_response;  
    double o2_hypoxic_saturation; 
    
    double o2_proliferation_saturation;  
    double o2_proliferation_threshold;  

    double o2_reference; 
    
    double o2_necrosis_threshold;  
    double o2_necrosis_max;  
    
    Phenotype* pReference_live_phenotype;  

    double max_necrosis_rate; 
    int necrosis_type;  
    
    Cell_Parameters(); 
}</code></pre>
<p>Here are the main data elements and member functions, in greater detail:</p>
<ol>
<li><p><strong><code>double o2_hypoxic_threshold</code></strong> is the oxygen value (in mmHg) below which hypoxic signaling starts. (default: 15 mmHg, or about 2% oxygen).</p>
<p><span class="math display">$$\verb|o2_hypoxic_saturation| \le \verb|o2_hypoxic_response| \le \verb|o2_hypoxic_threshold|$$</span></p></li>
<li><p><strong><code>double o2_hypoxic_response</code></strong> is the oxygen value (in mmHg) below which hypoxic responses are observed (e.g., omics changes). (default: 8 mmHg)</p>
<p><span class="math display">$$\verb|o2_hypoxic_saturation| \le \verb|o2_hypoxic_response| \le \verb|o2_hypoxic_threshold|$$</span></p></li>
<li><p><strong><code>double o2_hypoxic_saturation</code></strong> is the oxygen value (in mmHg) below which hypoxic responses are at a maximum. (default: 4 mmHg)</p>
<p><span class="math display">$$\verb|o2_hypoxic_saturation| \le \verb|o2_hypoxic_response| \le \verb|o2_hypoxic_threshold|$$</span></p></li>
<li><p><strong><code>double o2_proliferation_saturation</code></strong> is the oxygen value (in mmHg) above which the proliferation rate is maximmized. No further oxygenation benefits the cell. (default: 160 mmHg, or 21% standard culture conditions)</p>
<p><span class="math display">$$\verb|o2_proliferation_threshold| \le \verb|o2_reference| \le \verb|o2_proliferation_saturation|$$</span></p></li>
<li><p><strong><code>double o2_proliferation_threshold</code></strong> is the oxygen value (in mmHg) below which the proliferation ceases. (default: 5 mmHg)</p>
<p><span class="math display">$$\verb|o2_proliferation_threshold| \le \verb|o2_reference| \le \verb|o2_proliferation_saturation|$$</span></p></li>
<li><p><strong><code>double o2_reference</code></strong> is the oxygen value that corresponds to the reference phenotype (see below). (default: 160 mmHg)</p>
<p><span class="math display">$$\verb|o2_proliferation_threshold| \le \verb|o2_reference| \le \verb|o2_proliferation_saturation|$$</span></p></li>
<li><p><strong><code>double o2_necrosis_threshold</code></strong> is the oxygen value at which necrosis starts. (default: 5 mmHg)</p>
<p><span class="math display">$$\verb|o2_necrosis_max| \le \verb|o2_necrosis_threshold|$$</span></p></li>
<li><p><strong><code>double o2_necrosis_max</code></strong> is the oxygen value at which necrosis reaches its maximum rate. (default: 2.5 mmHg)</p>
<p><span class="math display">$$\verb|o2_necrosis_max| \le \verb|o2_necrosis_threshold|$$</span></p></li>
<li><p><strong><code>Phenotype* pReference_live_phenotype</code></strong> is a pointer to a <code>Phenotype</code> (See Section <a href="#sec:Phenotype" data-reference-type="ref" data-reference="sec:Phenotype">10</a>) which will serve as reference values when oxygen is equal to <code>o2_reference</code>.</p></li>
<li><p><strong><code>double max_necrosis_rate</code></strong> is the necrosis rate (in units 1/min) when the oxygen value dips below <code>o2_necrosis_max</code>.</p></li>
<li><p><strong><code>int necrosis_type</code></strong> is used to decide between deterministic and stochastic necrosis. (Use <code>PhysiCell_constants::deterministic_necrosis</code> or <code>PhysiCell_constants::stochastic_necrosis</code>.)</p></li>
<li><p><strong><code>Cell_Parameters()</code></strong> is the default constructor.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Cell_Functions">Cell_Functions</h3>
<p>This data structure attaches user-specified functions for key cell behaviors. Note that in PhysiCell, almost all functions that act on cells take the form</p>
<div class="center">
<p><code>void function( Cell* pCell, Phenotype&amp; phenotype, double dt )</code>.</p>
</div>
<p>Ordinarily, <code>phenotype = pCell-&gt;phenotype</code>, but we allow these to be specified separately for cases where <code>pCell = NULL</code>.</p>
<p>Here is the full class definition:</p>
<pre><code>class Cell_Functions
{
 private:
 public:
    Cycle_Model cycle_model; 

    void (*volume_update_function)( Cell* pCell, Phenotype&amp; phenotype , double dt );  
    void (*update_migration_bias)( Cell* pCell, 
        Phenotype&amp; phenotype, double dt ); 
    
    void (*custom_cell_rule)( Cell* pCell, Phenotype&amp; phenotype, double dt ); 
    void (*update_phenotype)( Cell* pCell, Phenotype&amp; phenotype, double dt );  
    
    void (*update_velocity)( Cell* pCell, Phenotype&amp; phenotype, double dt ); 
    
    void (*add_cell_basement_membrane_interactions)(Cell* pCell, 
        Phenotype&amp; phenotype, double dt );
    double (*calculate_distance_to_membrane)( Cell* pCell, 
        Phenotype&amp; phenotype, double dt );
    
    void (*set_orientation)(Cell* pCell, Phenotype&amp; phenotype, double dt );
    
    Cell_Functions();  
};</code></pre>
<p>Here are the member data and functions in greater detail:</p>
<ol>
<li><p><strong><code>Cycle_Model cycle_model</code></strong> is the cell cycle model to be used for this cell (or <code>Cell_Definition</code>–see Section <a href="#sec:Cell_Definition" data-reference-type="ref" data-reference="sec:Cell_Definition">9.4.5</a>). The <code>Cycle\_Model</code> class is discussed in greater detail in Section <a href="#sec:Cycle_Model" data-reference-type="ref" data-reference="sec:Cycle_Model">11.1.3</a>.</p></li>
<li><p><strong><code>void (*volume_update_function)( Cell* pCell, Phenotype&amp; phenotype, double dt )</code></strong> is a function pointer to a user-specified model of cell volume regulation, based upon the parameters stored in <code>phenotype.volume</code>. See Section <a href="#sec:Volume" data-reference-type="ref" data-reference="sec:Volume">11.3</a> for more detail. We recommend the reference model in <span class="citation" data-cites="ref:PhysiCell"></span>: <code>standard_volume_update_function</code>.</p></li>
<li><p><strong><code>void (*update_migration_bias)( Cell* pCell, Phenotype&amp; phenotype, double dt )</code></strong> is a function pointer to a user-specified model to set the migration bias direction, e.g., towards a chemical gradient. See Section <a href="#sec:Motility" data-reference-type="ref" data-reference="sec:Motility">11.6</a> for more detail. We give an example in Section <a href="#sec:Examples:migration" data-reference-type="ref" data-reference="sec:Examples:migration">19.1.2</a>.</p></li>
<li><p><strong><code>void (*custom_cell_rule)( Cell* pCell, Phenotype&amp; phenotype, double dt )</code></strong> is a custom function that is executed every time the cell updates its mechanics. We give an example in Section <a href="#sec:Examples:custom_rule" data-reference-type="ref" data-reference="sec:Examples:custom_rule">19.1.3</a></p></li>
<li><p><strong><code>void (*update_phenotype)( Cell* pCell, Phenotype&amp; phenotype, double dt )</code></strong> is where users should alter the cell’s phenotype based upon microenvironmental conditions. We give an example in Section <a href="#sec:Examples:phenotype_rule" data-reference-type="ref" data-reference="sec:Examples:phenotype_rule">19.1.4</a>. We recommend the reference model<br />
<code>update_cell_and_death_parameters_O2_based</code> found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p></li>
<li><p><strong><code>void (*update_velocity)( Cell* pCell, Phenotype&amp; phenotype, double dt )</code></strong> is a pointer to a user-specified model to set the cell’s velocity, based upon the mechanics model. We recommend <code>standard_update_cell_velocity</code> from <span class="citation" data-cites="ref:PhysiCell"></span>.</p></li>
<li><p><strong><code>void (*add_cell_basement_membrane_interactions)(Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> modifies the cell’s velocity based upon interactions with basement membrane given in this function. This function may change in future releases.</p></li>
<li><p><strong><code>double (*calculate_distance_to_membrane)( Cell* pCell, Phenotype&amp; phenotype, double dt );</code></strong> calculates the (signed) distance to the basement membrane (e.g., by an analytic solution, via a level set function, or by other discrete means).</p></li>
<li><p><strong><code>void (*set_orientation)(Cell* pCell, Phenotype&amp; phenotype, double dt )</code></strong> is a user-supplied function to update the cell’s orientation, based upon interactions wiht other neighbors or other factors.</p></li>
<li><p><strong><code>Cell_Functions()</code></strong> is the default constructor.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Cell_State">Cell_State</h3>
<p>The <code>Cell_State</code> is a small collection of cell descriptors that do not neatly belong in the cell <code>Phenotype</code>. Here is the full class definition:</p>
<pre><code>class Cell_State
{
 public:
    std::vector&lt;Cell*&gt; neighbors;   
    std::vector&lt;double&gt; orientation;
    
    double simple_pressure; 
    
    Cell_State(); 
};</code></pre>
<p>And here are further details on the member data and functions:</p>
<ol>
<li><p><strong><code>std::vector&lt;Cell*&gt; neighbors</code></strong> is the memory addresses of all cells that are currently neighbors of the cell (as determined by the adhesion interaction potential). <strong>This variable is not currently updated in PhysiCell, but it will be in a future release.</strong></p></li>
<li><p><strong><code>std::vector&lt;double&gt; orientation</code></strong> is the cell’s current basal-to-apical orientation, as a unit vector. Please note that if the cell’s <code>phenotype.geometry.polarity = 0</code>, then this state variable has no meaning. Also note that in 2-D simulations, one should set <code>orientation = {0,0,1}</code>.</p></li>
<li><p><strong><code>double simple_pressure</code></strong> is a simple analog for mechanical pressure, nondimensionalized by a scale. We define the dimensional pressure <span class="math inline"><em>p</em><sub><em>i</em></sub></span> by <span class="math display">$$p_i = \frac{1}{ S_i} \sum_{ j \in \mathcal{N}_i } \left|\mathbf{F}^\textrm{ccr}_{ij}\right|$$</span> where <span class="math inline">𝒩<sub><em>i</em></sub></span> is the set of the neighbor cells of the cell, <span class="math inline"><strong>F</strong><sub><em>i</em><em>j</em></sub><sup>ccr</sup></span> is the cell-cell “repulsive” imparted on cell <span class="math inline"><em>i</em></span> by its neighbor <span class="math inline"><em>j</em></span>, and <span class="math inline"><em>S</em><sub><em>i</em></sub></span> is the cell surface area. In <span class="citation" data-cites="macklin12_jtb ref:PhysiCell"></span>, we approximated <span class="math inline"><strong>F</strong><sub><em>i</em><em>j</em></sub><sup>ccr</sup></span> by <span class="math display">$$\mathbf{F}_{ij}^\mathrm{ccr} = 
c^\mathrm{ccr}_j \left( 1 - \frac{d_{ij}}{R_i+R_j} \right)^2 \frac{ \mathbf{d}_{ij} }{ d_{ij}},$$</span> where <span class="math inline"><strong>d</strong><sub><em>i</em><em>j</em></sub> = <strong>x</strong><sub><em>j</em></sub> − <strong>x</strong><sub><em>i</em></sub></span> and <span class="math inline"><em>d</em><sub><em>i</em><em>j</em></sub> = |<strong>d</strong><sub><em>i</em><em>j</em></sub>|</span>.</p>
<p>To define a scale, suppose the cell is in close packing in 3D by equally-sized cells with total volume <span class="math inline"><em>V</em></span>, mean radius <span class="math inline"><em>R</em></span>, maximal cross-sectional area <span class="math inline"><em>A</em></span>, and equal coefficient <span class="math inline"><em>c</em><sub><em>c</em><em>c</em><em>r</em></sub><sup><em>j</em></sup> = <em>c</em><sub><em>c</em><em>c</em><em>r</em></sub><sup><em>i</em></sup></span> for each neighbor <span class="math inline"><em>j</em></span>. In 3D, the cell has 12 neighbors in a tight sphere packing. By <span class="citation" data-cites="hyun13_jtb"></span>, the equilibrium cell-cell distance <span class="math inline"><em>s</em></span> in a 3-D confluent cell packing is <span class="math display">$$\begin{aligned}
\frac{s}{2R} &amp; = &amp; \frac{1}{2R}\sqrt{ \frac{2A}{\sqrt{3}} }  
= 
\sqrt{ \frac{2\pi R^2}{ 4R^2 \sqrt{3}} }  
= 
\sqrt{ \frac{\pi}{2 \sqrt{3}}  } \approx 0.9523. \end{aligned}$$</span></p>
<p>This defines a pressure scale: <span class="math display">$$\overline{p}_i = 12 \frac{c_\textrm{ccr}^i}{S_i} \left( 1 - \sqrt{\frac{\pi}{2\sqrt{3}}} \right)^2  \approx  
0.02729 \frac{c_\mathrm{ccr}^i}{S_i} .$$</span></p>
<p>Thus, we define a dimensionless analog of pressure by: <span class="math display">$$\begin{aligned}
\verb|simple_pressure| = 
\frac{ p_i }{ \overline{p}_i }
 &amp; = &amp; 
 \frac{1}{ \left( 1 - \sqrt{\frac{\pi}{2\sqrt{3}}} \right)^2 }
\sum_{j \in \mathcal{N}_i}{ \frac{c^j_\mathrm{ccr}}{c^i_\mathrm{ccr}}
\left( 1 - \frac{d_{ij}}{R_i + R_j} \right)^2 
} \nonumber  \\
&amp; = &amp;
 \frac{2\sqrt{3}}{ \left( \sqrt{2\sqrt{3}} - \sqrt{\pi} \right)^2 }
\sum_{j \in \mathcal{N}_i}{  \frac{c^j_\mathrm{ccr}}{c^i_\mathrm{ccr}}
\left( 1 - \frac{d_{ij}}{R_i + R_j} \right)^2 
} \nonumber \\ 
&amp; \approx &amp;  
439.74 \sum_{j \in \mathcal{N}_i}{
  \frac{c^j_\mathrm{ccr}}{c^i_\mathrm{ccr}}
  \left( 1 - \frac{d_{ij}}{R_i + R_j} \right)^2 
} \nonumber \\
&amp; = &amp; 
\frac{439.74}{c^i_\mathrm{ccr}} \sum_{j \in \mathcal{N}_i}{
 {c^j_\mathrm{ccr}} \left( 1 - \frac{d_{ij}}{R_i + R_j} \right)^2 
} .\end{aligned}$$</span></p></li>
<li><p><strong><code>Cell_State()</code></strong> is the default constructor.</p></li>
</ol>
<h3 id="sec:Cell_Definition">Cell Definition</h3>
<p>The <code>Cell_Definition</code> class allows users to define a cell type, including its default phenotype, and all its custom functions. Users can then work on defining multiple cell types at the start of a simulation and using these to initialize many cells at the start of a simulation (or during a simulation).</p>
<p>Here is the full class definition:</p>
<pre><code>class Cell_Definition
{
 private:
 public: 
    int type; 
    std::string name; 
 
    Microenvironment* pMicroenvironment; 
    
    Cell_Parameters parameters; 
    Custom_Cell_Data custom_data; 
    Cell_Functions functions; 
    Phenotype phenotype; 

    Cell_Definition();   
};</code></pre>
<p>Here are the member data and functions in greater detail:</p>
<ol>
<li><p><strong><code>int type</code></strong> is a unique identifier for the cell type. It will be copied to the cell’s <code>type</code>.</p></li>
<li><p><strong><code>std::string name</code></strong> is the “plain English” name of the cell type. It is copied to the cell’s <code>type_name</code>.</p></li>
<li><p><strong><code>pMicroenvironment</code></strong> is a pointer to the simulation’s BioFVM microenvironment, which is always <code>&amp;microenvironment</code>.</p></li>
<li><p><strong><code>parameters</code></strong> is defined in Section <a href="#sec:Cell_Parameters" data-reference-type="ref" data-reference="sec:Cell_Parameters">9.4.2</a>. It is copied to the cell’s <code>parameters</code>.</p></li>
<li><p><strong><code>custom_data</code></strong> is defined in Section <a href="#sec:Custom_Cell_Data" data-reference-type="ref" data-reference="sec:Custom_Cell_Data">9.4.1</a>. It is copied to the cell’s <code>custom_data</code>.</p></li>
<li><p><strong><code>functions</code></strong> is defined in Section <a href="#sec:Cell_Functions" data-reference-type="ref" data-reference="sec:Cell_Functions">9.4.3</a>. It is copied to the cell’s <code>functions</code>.</p></li>
<li><p><strong><code>phenotype</code></strong> is defined in Section <a href="#sec:Phenotype" data-reference-type="ref" data-reference="sec:Phenotype">10</a>. It is copied to the cell’s <code>phenotype</code>.</p></li>
<li><p><strong><code>Cell_Definition()</code></strong> is the default constructor.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:Phenotype">Phenotype </h1>
<p>The <code>Phenotype</code> is one of the most important components of a cell in PhysiCell, allowing us to specify the current state and properties of a cell. Most functions in PhysiCell are based upon either updating the phenotype or advancing the simulation based upon each cell’s current phenotype.</p>
<p>The <code>Phenotype</code> is divided into multiple functional groups:</p>
<ol>
<li><p><strong>Cycle</strong> gives cell cycle information, including the graph structure of the cycle model, associated parameter values (transition rates), and information on the current cycle phase. See Section <a href="#sec:Cycle" data-reference-type="ref" data-reference="sec:Cycle">11.1</a>. Note that for a dead cell, the “cycle model” is set to a death model.</p></li>
<li><p><strong>Death</strong> gives current cell death rates for one or more death models. See Section <a href="#sec:Death" data-reference-type="ref" data-reference="sec:Death">11.2</a>.</p></li>
<li><p><strong>Volume</strong> gives the cell’s current total volume, as well as nuclear, cytoplasmic, fluid, and other sub-volumes. See Section <a href="#sec:Volume" data-reference-type="ref" data-reference="sec:Volume">11.3</a>.</p></li>
<li><p><strong>Geometry</strong> records the cell’s radius, nuclear radius, and surface area (using spherical approximations). See Section <a href="#sec:Geometry" data-reference-type="ref" data-reference="sec:Geometry">11.4</a>.</p></li>
<li><p><strong>Mechanics</strong> records the cell’s adhesion and repulsion strength parameters for interactions with cells and the basement membrane, as well as the maximum adhesive interaction distance (a multiple of the cell’s equivalent radius). Future releases of PhysiCell will likely expand this aspect of the cell phenotype. See Section <a href="#sec:Mechanics" data-reference-type="ref" data-reference="sec:Mechanics">11.5</a>.</p></li>
<li><p><strong>Motility</strong> records phenotype information on motility, currently including persistence, a direction for biased random walks (e.g., chemotaxis), and a scalar bias parameter that can vary motility between purely Brownian and completely deterministic along the current bias direction. See Section <a href="#sec:Motility" data-reference-type="ref" data-reference="sec:Motility">11.6</a>.</p></li>
<li><p><strong>Secretion</strong> records cell secretion/export and uptake rates, as well as a saturation density (at which secretion ends). See Section <a href="#sec:Secretion" data-reference-type="ref" data-reference="sec:Secretion">11.7</a>.</p></li>
<li><p><strong>Molecular</strong> is used to model molecular-scale details, particularly tracking internalized substrates. In future versions of PhysiCell, molecular-scale models (e.g., SBML models) will likely be attached here. See Section <a href="#sec:phenotype_molecular" data-reference-type="ref" data-reference="sec:phenotype_molecular">11.8</a>.</p></li>
</ol>
<p>Here is how the <code>Phenotype</code> class is defined in <code>PhysiCell_phenotype.h</code>:</p>
<pre><code>class Phenotype
{
 private:
 public:
    bool flagged_for_division; 
    bool flagged_for_removal; 
 
    Cycle cycle; 
    Death death; 
    Volume volume; 
    Geometry geometry; 
    Mechanics mechanics; 
    Motility motility; 
    Secretion secretion; 
    Molecular molecular; 
    
    Phenotype();   
    
    void sync_to_functions( Cell_Functions&amp; functions ); 
    
    void sync_to_microenvironment( Microenvironment* pMicroenvironment ); 
    
    void sync_to_default_functions( void );   
};</code></pre>
<p>In the Section <a href="#sec:phenotype_details" data-reference-type="ref" data-reference="sec:phenotype_details">11</a>, we give further details on the data elements within the <code>Phenotype</code> class.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="member-functions">Member functions </h2>
<ol>
<li><p><strong><code>Phenotype()</code></strong> is the default constructor.</p></li>
<li><p><strong><code>void sync_to_functions( Cell_Functions&amp; functions )</code></strong> makes sure that <code>phenotype.cycle</code> is matched to the cycle model and parameters in <code>functions.cycle_model</code>. See Section <a href="#sec:Cycle" data-reference-type="ref" data-reference="sec:Cycle">11.1</a> for more details on the cycle model.</p></li>
<li><p><strong><code>void sync_to_microenvironment( Microenvironment* pMicroenvironment )</code></strong> bundles all functions (currently in <code>Secretion</code> and <code>Molecular</code>) that need to sync the phenotype with the microenvironment. This function is not yet needed, as syncing is performed automatically in the appropriate constructors.</p></li>
<li><p><strong><code>void sync_to_default_functions( void )</code></strong> is neither implemented nor used, because default constructors take care of this. The function will be deprecated.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:phenotype_details">Phenotype details</h1>
<h2 id="sec:Cycle">Cycle Models</h2>
<p><code>Cycle</code> stores the graph structure and parameters of the current cycle model, which can either be a cell cycle model or a death cycle model. It also includes member functions to progress through the cycle, and call appropriate cell division or removal functions. Before introducing <code>Cycle</code> (Section <a href="#sec:Cycle_Class" data-reference-type="ref" data-reference="sec:Cycle_Class">11.1.5</a>), we will detail the sub-classes necessary to work with a cycle model. All these data structures have been introduced with the goal of separating the graph structure of a cycle model (<code>Cycle_Model</code>: Section <a href="#sec:Cycle_Model" data-reference-type="ref" data-reference="sec:Cycle_Model">11.1.3</a>) from its parameter values (<code>Cycle_Data</code>: section <a href="#sec:Cycle_Data" data-reference-type="ref" data-reference="sec:Cycle_Data">11.1.4</a>), while still bundling them in a simple structure (<code>Cycle</code>: Section <a href="#sec:Cycle_Class" data-reference-type="ref" data-reference="sec:Cycle_Class">11.1.5</a>) for use in a <code>Phenotype</code>.</p>
<p>A <code>Cycle_Model</code> is constructed of one or more <code>Phase</code>s (Section <a href="#sec:Phase" data-reference-type="ref" data-reference="sec:Phase">11.1.1</a>) that are connected into a directed graph by <code>Phase_Link</code>s (Section <a href="#sec:Phase_Link" data-reference-type="ref" data-reference="sec:Phase_Link">11.1.2</a>).</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Phase">Phase </h3>
<p>The <code>Phase</code> class defines the phase in a cycle model, including the following data elements:</p>
<ol>
<li><p><strong><code>int index</code></strong> is an internal unique index within a cycle model.</p></li>
<li><p><strong><code>int code</code></strong> is a unique global identifier for the phase, using constants defined in <code>PhysiCell_constants.h</code> using <code>PhysiCell_constants</code>. See Section <a href="#sec:PhysiCell_constants" data-reference-type="ref" data-reference="sec:PhysiCell_constants">16.7</a>.</p></li>
<li><p><strong><code>std::string name</code></strong> is the “plain English” name of the phase (e.g., G0/G1).</p></li>
<li><p><strong><code>bool division_at_phase_exit</code></strong> is a Boolean variable that indicates whether the cell should divide at the end of this phase (e.g., at the end of M phase).</p></li>
<li><p><strong><code>bool removal_at_phase_exit</code></strong> is a Boolean variable that indicates whether the cell should be removed at the end of this phase (e.g., at the end of apoptosis).</p></li>
<li><p><strong><code>void (*entry_function)(Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> is a pointer to a function that is executed at the start of the phase. This would be a good place to write a function to perform mutations (e.g., at the start of G0/G1, randomly choose selected phenotype parameters according to a distribution).</p></li>
</ol>
<p>Here is the formal class declaration:</p>
<pre><code>class Phase
{
 public:
     int index;
     int code; 
     std::string name; 
     
     bool division_at_phase_exit; 
     bool removal_at_phase_exit; 
     
     void (*entry_function)( Cell* pCell, Phenotype&amp; phenotype, double dt ); 
     
     Phase();
};</code></pre>
<h4 id="member-functions-1">Member functions</h4>
<ol>
<li><p><strong><code>Phase()</code></strong> is the default constructor. It sets <code>index = 0</code>, <code>code = 0</code>, <code>name = "unnamed"</code>, all flags to <code>false</code>, and the entry function to <code>NULL</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Phase_Link">Phase_Link </h3>
<p>The <code>Phase_Link</code> class is a link between one <code>Phase</code> and another (e.g., progression from G0/G1 to S phase). It includes the following data elements:</p>
<ol>
<li><p><strong><code>int start_phase_index</code></strong> is the unique index of the starting phase in the phase transition (a link from phase <code>start_phase_index</code> to phase <code>end_phase_index</code>).</p></li>
<li><p><strong><code>int end_phase_index</code></strong> is the unique index of the ending phase in the phase transition (a link from phase <code>start_phase_index</code> to phase <code>end_phase_index</code>).</p></li>
<li><p><strong><code>bool fixed_duration</code></strong> is a Boolean variable that indicates whether the cell spends a fixed amount of time before transitioning from phase <code>start_phase_index</code> to phase <code>end_phase_index</code>. Note that this variable only makes sense if there is a single, unique phase transition starting from <code>start_phase_index</code>.</p></li>
<li><p><strong><code>void (*arrest_function)(Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> is a function pointer that allows you to set an arrest condition for the phase transition (e.g., only progress from M to G0/G1 if the cell is of sufficient volume). Its return value is <code>true</code> if the transition is arrested, and <code>false</code> if the transition is allowed to proceed. Set this pointer to <code>NULL</code> to bypass checking for arrest in this phase link.</p></li>
<li><p><strong><code>void (*exit_function)(Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> is a function pointer to a function that is executed at the end of the phase transition. This would be a good place to write a function to perform mutations (e.g., at the transition from M to G0/G1, randomly choose selected phenotype parameters according to a distribution).</p></li>
</ol>
<p>Here is the formal class declaration:</p>
<pre><code>class Phase_Link
{
 public:
     int start_phase_index;
     int end_phase_index; 
     
     bool fixed_duration; 
     
     bool (*arrest_function)( Cell* pCell, Phenotype&amp; phenotype, double dt ); 
     void (*exit_function)(  Cell* pCell, Phenotype&amp; phenotype, double dt ); 
     
     Phase_Link(); 
};</code></pre>
<h4 id="member-functions-2">Member functions</h4>
<ol>
<li><p><strong><code>Phase_Link()</code></strong> is the default constructor. It sets all indices to 0, all flags to <code>false</code>, and it sets <code>arrest_function = NULL</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Cycle_Model">Cycle_Model </h3>
<p>The <code>Cycle_Model</code> connects one or more <code>Phase</code>s through <code>Phase_Link</code>s, and stores this entire graph structure along with parameter values. (See <code>Cycle_Data</code> in Section <a href="#sec:Cycle_Data" data-reference-type="ref" data-reference="sec:Cycle_Data">11.1.4</a>.) It also contains member functions to assist with constructing and executing a cycle model, as well as to readily access transition rates. Here are the key data elements:</p>
<ol>
<li><p><strong><code>std::vector&lt; std::unordered_map&lt;int,int&gt; &gt; inverse_index_maps</code></strong> is an internal (private) data structure for easily accessing specific phase transitions. For reference, <code>index_inverse_map[i][j] = k</code> helps us find the <code>Phase_Link</code> from <code>Phase</code> <span class="math inline"><em>i</em></span> to <code>Phase</code> <span class="math inline"><em>j</em></span>, which is stored in <code>phase_links[i][k]</code>, and whose transition rate is stored in <code>data.transition_rates[i][k]</code>.</p></li>
<li><p><strong><code>std::string name</code></strong> is the “plain English” name of the cycle model (e.g., Ki67 (Basic)).</p></li>
<li><p><strong><code>int code</code></strong> is a unique global (integer) identifier for the cycle model, using constants defined in <code>PhysiCell_constants.h</code> using <code>PhysiCell_constants</code>. (See Section <a href="#sec:PhysiCell_constants" data-reference-type="ref" data-reference="sec:PhysiCell_constants">16.7</a>.)</p></li>
<li><p><strong><code>std::vector&lt;Phases&gt; phases</code></strong> is a vector of <code>Phase</code>s.</p></li>
<li><p><strong><code>std::vector&lt; std::vector&lt;Phase_Link&gt; &gt; phase_links</code></strong> is a vector of vectors of <code>Phase_Link</code>s. Note that <code>phase_links[i]</code> is the vector of all phase links starting at phase <code>i</code>. (This is why we need the inverse map above.)</p></li>
<li><p><strong><code>int default_phase_index</code></strong> is the index of the default phase in the cycle model (usually 0). If a new <code>Phenotype</code> instance is created and assigned this cycle model, it should start out in this phase.</p></li>
<li><p><strong><code>Cycle_Data data</code></strong> (of type <code>Cycle_Data</code>) contains a template of the key parameter values for this cycle model. Place default values for your cycle model here, as a copy of <code>data</code> is passed to any new <code>Phenotype</code> instance containing the cycle model. See Section <a href="#sec:Cycle_Data" data-reference-type="ref" data-reference="sec:Cycle_Data">11.1.4</a>.</p></li>
</ol>
<p>Here is the formal class declaration:</p>
<pre><code>class Cycle_Model
{
 private:
     std::vector&lt; std::unordered_map&lt;int,int&gt; &gt; inverse_index_maps; 
 
 public:
     std::string name; 
     int code; 

     std::vector&lt;Phase&gt; phases; 
     std::vector&lt; std::vector&lt;Phase_Link&gt; &gt; phase_links; 
     
     int default_phase_index; 
     
     Cycle_Data data; 

     Cycle_Model(); 
     
     void advance_model( Cell* pCell, Phenotype&amp; phenotype, double dt ); 
     
     int add_phase( int code, std::string name ); 
     
     int add_phase_link( int start_index, int end_index , 
          bool (*arrest_function)( Cell* pCell, Phenotype&amp; phenotype, double dt ) ); 
     int add_phase_link( int start_index, int end_index , double rate , 
          bool (*arrest_function)( Cell* pCell, Phenotype&amp; phenotype, double dt ) ); 
            
     int find_phase_index( int code ); 
     int find_phase_index( std::string ); 
     
     double&amp; transition_rate( int start_index , int end_index ); 
     Phase_Link&amp; phase_link(int i,int j); 
     
     std::ostream&amp; display( std::ostream&amp; os ); 
};</code></pre>
<h4 id="member-functions-3">Member functions</h4>
<ol>
<li><p><strong><code>Cycle_Model()</code></strong> is the default constructor. It sets <code>name = "unnamed"</code>, sets <code>code = PhysiCell_constants::custom_cycle_model</code>, sets the model to an empty one with no phases, and the links <code>data.pCycle_Model</code> to <code>this</code> (the <code>Cycle_Model</code> under construction). See Section <a href="#sec:Cycle_Data" data-reference-type="ref" data-reference="sec:Cycle_Data">11.1.4</a>.</p></li>
<li><p><strong><code>int add_phase(int code, std::string name)</code></strong> adds a new <code>Phase</code> to the cycle model, with the supplied <code>code</code> and <code>name</code>. It returns the index (<code>new_index</code>) of the new phase, so that you can subsequently access it with <code>phases[new_index]</code>.</p></li>
<li><p><strong><code>int add_phase_link( int start_index, int end_index, bool (*arrest_function)( Cell* pCell, Phenotype&amp; phenotype, double dt ) )</code></strong><br />
adds a new <code>Phase_Link</code> to <code>phase_links[start_index]</code> joining phase <code>start_index</code> to phase <code>end_index</code>, with the arrest function <code>arrest_function</code>. It resizes internal data structures including <code>data</code> (and its <code>transition_rates</code>) automatically, and sets the transition rate to 0.0. It returns the index (<code>new_index</code>) so that the phase link can be directly accessed as <code>phase_links[start_index][new_index]</code>.</p></li>
<li><p><strong><code>int add_phase_link( int start_index, int end_index, double rate bool (*arrest_function)( Cell* pCell, Phenotype&amp; phenotype, double dt ) )</code></strong><br />
adds a new <code>Phase_Link</code> to <code>phase_links[start_index]</code> joining phase <code>start_index</code> to phase <code>end_index</code>, with the arrest function <code>arrest_function</code>. It resizes internal data structures including <code>data</code> (and its <code>transition_rates</code>) automatically, and sets the transition rate to <code>rate</code>. It returns the index (<code>new_index</code>) so that the phase link can be directly accessed as <code>phase_links[start_index][new_index]</code>.</p></li>
<li><p><strong><code>int find_phase_index( int code )</code></strong> finds the index <code>i</code> such that <code>phases[i].code = code</code>. Please note that this returns 0 if there is no exact match!</p></li>
<li><p><strong><code>int find_phase_index( std::string name )</code></strong> finds the index <code>i</code> such that <code>phases[i].name = name</code>. Please note that this returns 0 if there is no exact match! Note that this function is case sensitive.</p></li>
<li><p><strong><code>double&amp; transition_rate( int start_index , int end_index )</code></strong> is a user-friendly interface function to access (by reference) the transition rate from phase <code>start_index</code> to phase <code>end_index</code>.</p></li>
<li><p><strong><code>Phase_Link&amp; phase_link(int start_index , int end_index)</code></strong> is a user-friendly interface function to access (by reference) the <code>Phase_Link</code> from phase <code>start_index</code> to phase <code>end_index</code>.</p></li>
<li><p><strong><code>void advance_model( Cell* pCell, Phenotype&amp; phenotype, double dt )</code></strong> advances the the cycle model by <code>dt</code> time (assumed minutes in current PhysiCell versions). For the current phase in <code>phenotype.cycle.data.current_phase()</code>, it evaluates the probability of advancing to all linked phases within <code>dt</code> time (see <span class="citation" data-cites="ref:PhysiCell"></span>) and changes the model (and the state of <code>phenotype.cycle.data</code>) accordingly. It will call cell division and removal functions as needed.</p></li>
<li><p><strong><code>std::ostream&amp; display( std::ostream&amp; os )</code></strong> allows streaming of a basic visual output of the cycle model. I recommend calling <code>display( std::cout )</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Cycle_Data">Cycle_Data </h3>
<p>The <code>Cycle_Data</code> class contains key parameters and state variables for a cell cycle model (see Section <a href="#sec:Cycle_Model" data-reference-type="ref" data-reference="sec:Cycle_Model">11.1.3</a>), as well as member functions to easily access transition rates and the current cycle phase. It includes the following data elements:</p>
<ol>
<li><p><strong><code>std::vector&lt; std::unordered_map&lt;int,int&gt; &gt; inverse_index_maps</code></strong> is an internal (private) data structure for easily accessing specific phase transitions. For reference, <code>index_inverse_map[i][j] = k</code> helps us find the <code>Phase_Link</code> from <code>Phase</code> <span class="math inline"><em>i</em></span> to <code>Phase</code> <span class="math inline"><em>j</em></span> in the <code>pCycle_Model</code>, which is stored in <code>pCycle_Model-&gt;phase_links[i][k]</code>, and whose transition rate is stored in <code>transition_rates[i][k]</code>.</p></li>
<li><p><strong><code>Cycle_Model* pCycle_Model</code></strong> is a pointer to the appropriate <code>Cycle_Model</code>.</p></li>
<li><p><strong><code>std::string time_units</code></strong> is the units of time for the cycle model. (PhysiCell currently assumes all time units are in minutes.)</p></li>
<li><p><strong><code>std::vector&lt; std::vector&lt;double&gt; &gt; transition_rates</code></strong> is a vector of vectors of cell phase transition rates. For each <code>i</code>, <code>transition_rates[i]</code> is the vector of transition rates from Phase <code>i</code> to any other linked phases. For safety, we might make this data element private in the future, as it can be more intuitively accessed via <code>double&amp; transition_rate(int,int)</code> (below).</p></li>
<li><p><strong><code>int current_phase_index</code></strong> indicates the current phase in the <code>Cycle_Model</code>.</p></li>
<li><p><strong><code>double elapsed_time_in_phase</code></strong> records how long the cell has been in the current phase.</p></li>
</ol>
<p>Here is the formal class declaration:</p>
<pre><code>class Cycle_Data
{
 private:
    std::vector&lt; std::unordered_map&lt;int,int&gt; &gt; inverse_index_maps; 

 public:
    Cycle_Model* pCycle_Model; 

    std::string time_units; 
 
    std::vector&lt; std::vector&lt;double&gt; &gt; transition_rates; 
    
    int current_phase_index; 
    double elapsed_time_in_phase; 
    
    Cycle_Data();  
    
    Phase&amp; current_phase( void );      
    
    void sync_to_cycle_model( void );      

    double&amp; transition_rate(int start_phase_index, int end_phase_index );     
    double&amp; exit_rate(int phase_index ); 
};</code></pre>
<h4 id="member-functions-4">Member functions</h4>
<ol>
<li><p><strong><code>Cycle_Data()</code></strong> is the default constructor. It resizes <code>transition_rates</code> to zero, sets <code>pCycle_Model = NULL</code>, and defaults <code>time_units = "min"</code>.</p></li>
<li><p><strong><code>Phase&amp; current_phase( void )</code></strong> is a user-friendly interface function to access (by reference) the current <code>Phase</code> in the cycle. Use this to get the name and other structural information.</p></li>
<li><p><strong><code>void sync_to_cycle_model( void )</code></strong> resizes the internal data structures for consistency with the <code>pCycle_Model</code>, if it is non-<code>NULL</code>.</p></li>
<li><p><strong><code>double&amp; transition_rate( int start_phase_index , int end_phase_index )</code></strong> is a user-friendly interface function to access (by reference) the transition rate from phase <code>start_phase_index</code> to phase <code>end_phase_index</code>.</p></li>
<li><p><strong><code>double&amp; exit_rate( int phase_index )</code></strong> is a user-friendly interface function to access (by reference) the rate of exiting the <code>phase_index</code> phase, in the case where there is only one <code>Phase_Link</code> from that phase to another. (e.g., for a cycle model where the S phase only links to the G2 phase.) In this case, the cell spends (in the mean) <span class="math display">$$\frac{1}{\texttt{exit\_rate}(\texttt{phase\_index}) }$$</span> time in phase <code>phase_index</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Cycle_Class">Cycle </h3>
<p>The <code>Cycle</code> bundles a <code>Cycle_Model</code> with <code>Cycle_Data</code> for simpler inclusion in a <code>Phenotype</code>. Its main data elements are:</p>
<ol>
<li><p><strong><code>Cycle_Model* pCycle_Model</code></strong> is a pointer to a <code>Cycle_Model</code>.</p></li>
<li><p><strong><code>Cycle_Data data</code></strong> is <code>Cycle_Data</code> associated with the <code>Cycle_Model</code>. Note that this is an <em>independent copy</em> of the <code>pCycle_Model-&gt;data</code>, so that a single cell’s phenotype can be updated without modifying the defaults for the underlying cycle model.</p></li>
</ol>
<p>Here is the formal class declaration:</p>
<pre><code>class Cycle
{
 private:
 public:
    Cycle_Model* pCycle_Model; 
    Cycle_Data data; 
    
    Cycle();     
    
    void advance_cycle( Cell* pCell, Phenotype&amp; phenotype, double dt );      
    
    Cycle_Model&amp; model( void );      
    Phase&amp; current_phase( void );      
    int&amp; current_phase_index( void );      
    
    void sync_to_cycle_model( Cycle_Model&amp; cm );      
};</code></pre>
<h4 id="member-functions-5">Member functions</h4>
<ol>
<li><p><strong><code>Cycle()</code></strong> is the default constructor. It sets <code>pCycle_Model = NULL</code> and uses the default constructor for the <code>Cycle_Data</code>.</p></li>
<li><p><strong><code>void advance_cycle(Cell* pCell, Phenotype&amp; phenotype, double dt </code></strong> advances the cycle model by <code>dt</code> time, executing any arrest, entry, or other functions according to the supplied phenotype. (It is implemented by calling <code>pCycle_Model-&gt;advance_model(pCell,phenotype,dt)</code>.</p></li>
<li><p><strong><code>Cycle_Model&amp; model(void)</code></strong> returns (by reference) the cycle model pointed to by <code>pCycle_Model</code>.</p></li>
<li><p><strong><code>Phase&amp; current_phase(void)</code></strong> returns (by reference) the current phase (as given in <code>data</code>) in the cycle model.</p></li>
<li><p><strong><code>int&amp; current_phase_index(void)</code></strong> returns (by reference) the current phase index (as given in <code>data</code>) in the cycle model.</p></li>
<li><p><strong><code>void sync_to_cycle_model(Cycle_Model&amp; cm)</code></strong> sets <code>pCycle_Model = &amp;cm</code> and then overwrites <code>data</code> with <code>cm.data</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Death">Death models </h2>
<p>A death model is a <code>Cycle_Model</code> (Section <a href="#sec:Cycle_Model" data-reference-type="ref" data-reference="sec:Cycle_Model">11.1.3</a>), where one of the phases is marked to trigger cell removal. We define <code>Death_Parameters</code> (Section <a href="#sec:Death_Parameters" data-reference-type="ref" data-reference="sec:Death_Parameters">11.2.1</a>) to include key parameters needed in most death models, and bundle these as <code>Death</code> (Section <a href="#sec:Death_Class" data-reference-type="ref" data-reference="sec:Death_Class">11.2.2</a>) within the phenotype, similarly to <code>Cycle</code> (Section <a href="#sec:Cycle_Class" data-reference-type="ref" data-reference="sec:Cycle_Class">11.1.5</a>).</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Death_Parameters">Death_Parameters </h3>
<p><code>Death_Parameters</code> bundles key parameters needed to initialize a cell death model, particularly changes in a cell’s volume model. The key data elements include:</p>
<ol>
<li><p><strong><code>std::string time_units</code></strong> gives the time units (by default minutes throughout PhysiCell).</p></li>
<li><p><strong><code>double unlysed_fluid_change_rate</code></strong> is the rate of fluid change (in <span class="math inline">min<sup> − 1</sup></span>) prior to cell lysis.</p></li>
<li><p><strong><code>double lysed_fluid_change_rate</code></strong> is the rate of fluid change (in <span class="math inline">min<sup> − 1</sup></span>) after cell lysis.</p></li>
<li><p><strong><code>double cytoplasmic_biomass_change_rate</code></strong> is the degradation rate for cytoplasmic solids (in <span class="math inline">min<sup> − 1</sup></span>).</p></li>
<li><p><strong><code>double nuclear_biomass_change_rate</code></strong> is the degradation rate for nuclear solids (in <span class="math inline">min<sup> − 1</sup></span>).</p></li>
<li><p><strong><code>double calcification_rate</code></strong> is the rate of cell calcification (in <span class="math inline">min<sup> − 1</sup></span>).</p></li>
<li><p><strong><code>double relative_rupture_volume</code></strong> is the relative amount by which the cell must swell (compared to the volume at the onset of cell death) before it bursts or lyses.</p></li>
</ol>
<p>Here is the formal class declaration:</p>
<pre><code>class Death_Parameters
{
 public:
    std::string time_units; 
 
    double unlysed_fluid_change_rate;
    double lysed_fluid_change_rate; 
    
    double cytoplasmic_biomass_change_rate;
    double nuclear_biomass_change_rate; 
    
    double calcification_rate; 
    
    double relative_rupture_volume; 
    
    Death_Parameters();      
};</code></pre>
<h4 id="member-functions-6">Member functions</h4>
<ol>
<li><p><strong><code>Death_Parameters()</code></strong> is the default constructor. It sets all parameter values to the reference apoptosis values for a generic breast epithelium line (calibrated to MCF-10A measurements), as in <span class="citation" data-cites="ref:PhysiCell"></span>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Death_Class">Death </h3>
<p>In PhysiCell, we allow the cells to evaluate multiple death models (e.g., apoptosis and necrosis). <code>Death</code> stores the cell’s death rates, the corresponding death models, and associated parameters. Here are the data elements:</p>
<ol>
<li><p><strong><code>std::vector&lt;double&gt; rates</code></strong> is a vector of death rates, one per death model.</p></li>
<li><p><strong><code>std::vector&lt;Cycle_Model*&gt; models</code></strong> is a vector of pointers to death models, which are of type <code>Cycle_Model</code>.</p></li>
<li><p><strong><code>std::vector&lt;Death_Parameters&gt; parameters</code></strong> is a vector of <code>Death_Parameters</code>s, one for each <code>Cycle_Model</code>.</p></li>
<li><p><strong><code>bool dead</code></strong> is a Boolean variable that is <code>true</code> if the cell is dead.</p></li>
<li><p><strong><code>int current_death_model_index</code></strong> is the index of the current death model, when <code>dead == true</code>.</p></li>
</ol>
<p>Here is the formal class declaration:</p>
<pre><code>class Death
{
 private:
 public:
    std::vector&lt;double&gt; rates; 
    std::vector&lt;Cycle_Model*&gt; models; 
    std::vector&lt;Death_Parameters&gt; parameters; 
    
    bool dead; 
    int current_death_model_index;
    
    Death();      
    
    int add_death_model( double rate, Cycle_Model* pModel );      
    int add_death_model( double rate, Cycle_Model* pModel, 
        Death_Parameters&amp; death_parameters);      
    
    int find_death_model_index( int code );      
    int find_death_model_index( std::string name );      
    
    bool check_for_death( double dt );     
    void trigger_death( int death_model_index );      
    
    Cycle_Model&amp; current_model( void );     
    Death_Parameters&amp; current_parameters( void );      
};</code></pre>
<h4 id="member-functions-7">Member functions</h4>
<ol>
<li><p><strong><code>Death()</code></strong> is the default construtor. It resizes all the vectors to size zero, sets <code>dead = false</code>, and <code>current_death_model_index = 0</code>.</p></li>
<li><p><strong><code>int add_death_model( double rate , Cycle_Model* pModel )</code></strong> adds the cycle model at<br />
<code>pModel</code> and sets its corresponding death rate to <code>rate</code>. It also resizes the <code>parameters</code> with values in the default constructor. It returns the index of the newly added death model.</p></li>
<li><p><strong><code>int add_death_model( double rate, Cycle_Model* pModel, Death_Parameters&amp; death_parameters)</code></strong> adds the cycle model at <code>pModel</code> and sets its corresponding death rate to <code>rate</code>. It also increases the size of <code>parameters</code> by one by appending <code>death_parameters</code>. It returns the index of the newly added death model.</p></li>
<li><p><strong><code>int find_death_model_index( int code )</code></strong> returns an integer <code>i</code> such that<br />
<code>models[i]-&gt;code == code</code>. Note that if no exact match is found, this returns 0.</p></li>
<li><p><strong><code>int find_death_model_index( std::string name )</code></strong> returns an integer <code>i</code> such that<br />
<code>models[i]-&gt;name == name</code>. Note that if no exact match is found, this returns 0. Note that this function is case sensitive.</p></li>
<li><p><strong><code>bool check_for_death( double dt )</code></strong> checks for each type of cell death in the next <code>dt</code> time. If the cell dies by any of the models between now and <code>dt</code> time in the future, this code sets <code>dead = true</code>, sets <code>current_death_model_index</code> to the index of the corresponding death model, and returns <code>true</code>.</p></li>
<li><p><strong><code>void trigger_death( int death_model_index )</code></strong> immediately sets the cell to <code>dead = true</code> and <code>current_death_model_index = death_model_index</code>.</p>
<p><span style="color: red"><strong>Note:</strong> this function is used internally by PhysiCell, but will not fully start cell death. Users should use </span> <code>Cell::start_death(int)</code> <span style="color: red"> instead. See Section <a href="#sec:cell_member_functions" data-reference-type="ref" data-reference="sec:cell_member_functions">9.2</a>.</span></p></li>
<li><p><strong><code>Cycle_Model&amp; current_model( void )</code></strong> returns (by reference) the current cell death model (if <code>dead == true</code>).</p></li>
<li><p><strong><code>Death_Parameters&amp; current_parameters( void )</code></strong> returns (by reference) the<br />
<code>Death_Parameters</code> for the current death model (if <code>dead == true</code>).</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Volume">Volume </h2>
<p><code>Volume</code> stores the cell’s total volume, its various sub-volume elements, and critical parameters. (PhysiCell supplies reasonable defaults.) Here are the main elements (all volume units in PhysiCell are currently assumed to be <span class="math inline"><em>μ</em>m<sup>3</sup></span>.)</p>
<ol>
<li><p><strong><code>double total</code></strong> is the cell’s total volume.</p></li>
<li><p><strong><code>double solid</code></strong> is the solid component of the cell’s total volume. It is in dimensional units of volume–not a fraction or ratio. Note that <code>volume.total = volume.solid + volume.fluid</code>.</p></li>
<li><p><strong><code>double fluid</code></strong> is the fluid component of the cell’s total volume. It is in dimensional units of volume–not a fraction or ratio. Note that <code>volume.total = volume.solid + volume.fluid</code>.</p></li>
<li><p><strong><code>double fluid_fraction</code></strong> is the fraction of the cell that is fluid, defined as:</p>
<p><code>volume.fluid_fraction = volume.fluid / volume.total</code>.</p>
<p>Note that <span class="math inline">0 ≤ <code>fluid_fraction</code> ≤ 1.</span></p></li>
<li><p><strong><code>double nuclear</code></strong> is the total nuclear volume. Note that:</p>
<p><code>volume.total = volume.nuclear + volume.cytoplasmic</code>.</p></li>
<li><p><strong><code>double nuclear_solid</code></strong> is the solid component of the cell’s nuclear volume. It is in dimensional units of volume–not a fraction or ratio. Note that:</p>
<p><code>volume.nuclear = volume.nuclear_solid + volume.nuclear_fluid</code>.</p></li>
<li><p><strong><code>double nuclear_fluid</code></strong> is the fluid component of the cell’s nuclear volume. It is in dimensional units of volume–not a fraction or ratio. Note that:</p>
<p><code>volume.nuclear = volume.nuclear_solid + volume.nuclear_fluid</code>.</p></li>
<li><p><strong><code>double cytoplasmic</code></strong> is the total cytoplasmic volume. Note that:</p>
<p><code>volume.total = volume.nuclear + volume.cytoplasmic</code>.</p></li>
<li><p><strong><code>double cytoplasmic_solid</code></strong> is the solid component of the cell’s cytoplasmic volume. It is in dimensional units of volume–not a fraction or ratio. Note that:</p>
<p><code>volume.cytoplasmic = volume.cytoplasmic_solid + volume.cytoplasmic_fluid</code>.</p></li>
<li><p><strong><code>double cytoplasmic_fluid</code></strong> is the fluid component of the cell’s cytoplasmic volume. It is in dimensional units of volume–not a fraction or ratio. Note that:</p>
<p><code>volume.cytoplasmic = volume.cytoplasmic_solid + volume.cytoplasmic_fluid</code>.</p></li>
<li><p><strong><code>double calcified_fraction</code></strong> is the fraction of the cell that is calcified. (This is particularly useful to simulations of ductal carcinoma in situ of the breast.) Note that</p>
<p><span class="math display">0 ≤ <code>calcified_fraction</code> ≤ 1.</span></p></li>
<li><p><strong><code>double cytoplasmic_to_nuclear_ratio</code></strong> is <code>volume.cytoplasmic / volume.nuclear</code>.</p></li>
<li><p><strong><code>double rupture_volume</code></strong> is the (dimensional) volume at which a cell will burst or lyse.</p></li>
<li><p><strong><code>double cytoplasmic_biomass_change_rate</code></strong> is the rate that cytoplasmic solid material can be synthesized to reach the target cytoplasmic solid volume. It is assumed to be written in units of <span class="math inline">min<sup> − 1</sup></span>.</p></li>
<li><p><strong><code>double nuclear_biomass_change_rate</code></strong> is the rate that nuclear solid material can be synthesized to reach the target nuclear solid volume. It is assumed to be written in units of <span class="math inline">min<sup> − 1</sup></span>.</p></li>
<li><p><strong><code>double fluid_change_rate</code></strong> is the rate that fluid can enter or leave the cell to reach the target fluid fraction. It is assumed to be written in units of <span class="math inline">min<sup> − 1</sup></span>.</p></li>
<li><p><strong><code>double calcification_rate</code></strong> is the rate that the cell calcifies. It is assumed to be written in units of <span class="math inline">min<sup> − 1</sup></span>.</p></li>
<li><p><strong><code>double target_solid_cytoplasmic</code></strong> is the cell’s target (“desired” or “goal”) solid cytoplasmic volume.</p></li>
<li><p><strong><code>double target_solid_nuclear</code></strong> is the cell’s target (“desired” or “goal”) solid nuclear volume.</p></li>
<li><p><strong><code>double target_fluid_fraction</code></strong> is the cell’s target (“desired” or “goal”) fluid fraction.</p></li>
<li><p><strong><code>double relative_rupture_volume</code></strong> is the relative volume at which a cell, written as a multiple of the cell’s total volume at the onset of a swelling process. (For example, at the start of necrosis.)</p></li>
</ol>
<p>Here is the class declaration:</p>
<pre><code>class Volume
{
 public:
    double total;
    double solid;
    double fluid;
    double fluid_fraction; 
    
    double nuclear;
    double nuclear_fluid;
    double nuclear_solid; 

    double cytoplasmic;
    double cytoplasmic_fluid; 
    double cytoplasmic_solid; 
    
    double calcified_fraction;
    
    double cytoplasmic_to_nuclear_ratio;
    
    double rupture_volume;  
    
    double cytoplasmic_biomass_change_rate; 
    double nuclear_biomass_change_rate; 
    double fluid_change_rate;

    double calcification_rate; 
    
    double target_solid_cytoplasmic;
    double target_solid_nuclear;
    double target_fluid_fraction;
    
    double target_cytoplasmic_to_nuclear_ratio;

    double relative_rupture_volume; 

    Volume();      
    
    void divide( void );      
    void multiply_by_ratio(double);      
    
    void update( Cell* pCell, Phenotype&amp; phenotype, double dt );      
};</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="member-functions-8">Member functions</h3>
<ol>
<li><p><strong><code>Volume()</code></strong> is the default constructor. It sets the variables to the reference values of a generic breast epithelium line (calibrated to MCF-10A).</p></li>
<li><p><strong><code>void divide(void)</code></strong> cuts the volume, all sub-volumes, and the target volumes by one half. (It is used during cell division.)</p></li>
<li><p><strong><code>void multiply_by_ratio(double ratio)</code></strong> multiplies the volume, all sub-volumes, and the target volumes by <code>ratio</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Geometry">Geometry </h2>
<p><code>Geometry</code> stores critical aspects of cell geometry other than volume. In the current implementation, we use spherical approximations for the cell geometry, since PhysiCell tracks cell volume but not cell morphology. The main data elements are:</p>
<ol>
<li><p><strong><code>double radius</code></strong> is the cell’s equivalent radius, based upon the spherical approximation <span class="math display">$$\texttt{volume.total} = \frac{4}{3} \pi \texttt{ radius}^3.$$</span></p>
<p>In the current version of PhysiCell, spatial units are assumed to be <span class="math inline"><em>μ</em>m</span>.</p></li>
<li><p><strong><code>double nuclear_radius</code></strong> is the nucleus’ equivalent radius, based upon the spherical approximation <span class="math display">$$\texttt{volume.nuclear} = \frac{4}{3} \pi \texttt{ nuclear\_radius}^3.$$</span> Its units are assumed <span class="math inline"><em>μ</em>m</span>.</p></li>
<li><p><strong><code>double surface_area</code></strong> is the cell’s equivalent surface area, based upon the spherical approximation</p>
<p><span class="math display"><code>surface_area</code> = 4<em>π</em><code> radius</code><sup>2</sup>.</span></p></li>
<li><p><strong><code>double polarity</code></strong> is a dimensionless number between 0 and 1 to indicate how polarized the cell is along its basal-to-apical axis. If the polarity is zero, the cell has no discernible polarity. Note that polarity should be set to one for 2-D simulations.</p>
<p>Its units are assumed <span class="math inline"><em>μ</em>m<sup>2</sup></span>.</p></li>
</ol>
<p>Here is the class definition in <code>PhysiCell_phenotype.h</code>:</p>
<pre><code>class Geometry
{
 public:
    double radius; 
    double nuclear_radius; 
    double surface_area; 
    
    double polarity; 
    
    Geometry();      
    
    void update_radius( Cell* pCell, Phenotype&amp; phenotype, double dt );      
    void update_nuclear_radius( Cell* pCell, Phenotype&amp; phenotype, double dt );      
    void update_surface_area( Cell* pCell, Phenotype&amp; phenotype, double dt );      
    
    void update( Cell* pCell, Phenotype&amp; phenotype, double dt );      
};</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="member-functions-9">Member functions</h3>
<ol>
<li><p><strong><code>Geometry()</code></strong> is the default constructor. It sets the variables to the reference values of a generic breast epithelium line (calibrated to MCF-10A).</p></li>
<li><p><strong><code>void update_radius( Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> sets<br />
<code>radius</code> according to the spherical approximation in Section <a href="#sec:Geometry" data-reference-type="ref" data-reference="sec:Geometry">11.4</a>, using <code>phenotype.volume.total</code>.</p></li>
<li><p><strong><code>void update_nuclear_radius( Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> sets<br />
<code>nuclear_radius</code> according to the spherical approximation in Section <a href="#sec:Geometry" data-reference-type="ref" data-reference="sec:Geometry">11.4</a>, using<br />
<code>phenotype.volume.nuclear</code>.</p></li>
<li><p><strong><code>void update_surface_area( Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> sets<br />
<code>surface_area</code> according to the spherical approximation in Section <a href="#sec:Geometry" data-reference-type="ref" data-reference="sec:Geometry">11.4</a>, using<br />
<code>cell.phenotype.volume.total</code>.</p></li>
<li><p><strong><code>void update( Cell* pCell, Phenotype&amp; phenotype, double dt)</code></strong> sets <code>radius</code>,<br />
<code>nuclear_radius</code>, and <code>surface_area</code> according to <code>phenotype.volume</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Mechanics">Mechanics </h2>
<p><code>Mechanics</code> stores the main mechanics parameters for a cell. The main data elements are:</p>
<ol>
<li><p><strong><code>double cell_cell_adhesion_strength</code></strong> is the parameter <span class="math inline"><em>C</em><sub>cca</sub></span> in the default PhysiCell mechanics model, written as a multiple of the drag coefficient <span class="math inline"><em>ν</em></span>; see <span class="citation" data-cites="ref:PhysiCell"></span>. It regulates the relative strength of cell-cell adhesive forces. Future releases of PhysiCell will allow this to be defined for interactions with multiple cell types.</p></li>
<li><p><strong><code>double cell_BM_adhesion_strength</code></strong> is the parameter <span class="math inline"><em>C</em><sub>cba</sub></span> in the default PhysiCell mechanics model, written as a multiple of the drag coefficient <span class="math inline"><em>ν</em></span>; see <span class="citation" data-cites="ref:PhysiCell"></span>. It regulates the relative strength of adhesion of cells to the basement membrane, when present.</p></li>
<li><p><strong><code>double cell_cell_repulsion_strength</code></strong> is the parameter <span class="math inline"><em>C</em><sub>ccr</sub></span> in the default PhysiCell mechanics model, written as a multiple of the drag coefficient <span class="math inline"><em>ν</em></span>; see <span class="citation" data-cites="ref:PhysiCell"></span>. It regulates the relative strength of cell-cell “repulsive” forces (resistance to deformation and compression).</p></li>
<li><p><strong><code>double cell_BM_repulsion_strength</code></strong> is the parameter <span class="math inline"><em>C</em><sub>cbr</sub></span> in the default PhysiCell mechanics model, written as a multiple of the drag coefficient <span class="math inline"><em>ν</em></span>; see <span class="citation" data-cites="ref:PhysiCell"></span>. It regulates the relative strength of cell-BM “repulsive” forces (resistance of cells to deformation and compression, and resistance of basement membranes to penetration and deformation by cells).</p></li>
<li><p><strong><code>double relative_maximum_adhesion_distance</code></strong> is the maximum distance of cell adhesion to other cells or a basement membrane, given as a (dimensionless) multiple of <code>geometry.radius</code>.</p></li>
</ol>
<p>As future releases of PhysiCell may include additional mechanics models, this class may be expanded in the future. In particular, we anticipate models to allow varying strengths of adhesion between different cell types, and improved adhesion models.</p>
<p>Here is the class definition in <code>PhysiCell_phenotype.h</code>:</p>
<pre><code>class Mechanics
{
 public:
    double cell_cell_adhesion_strength; 
    double cell_BM_adhesion_strength;
    double cell_cell_repulsion_strength;
    double cell_BM_repulsion_strength; 
    
    double relative_maximum_adhesion_distance; 
    double maximum_adhesion_distance;
    
    void set_relative_maximum_adhesion_distance( double new_value );  
    void set_relative_equilibrium_distance( double new_value );  
    
    void set_absolute_equilibrium_distance( Phenotype&amp; phenotype, double new_value );  
    
    Mechanics();      
};
</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="member-functions-10">Member functions</h3>
<ol>
<li><p><strong><code>Mechanics()</code></strong> is the default constructor function. It sets the parameters to the reference value for a generic breast epithelium line.</p></li>
<li><p><strong><code>void set_relative_maximum_adhesion_distance( double new_value )</code></strong> sets the new maximum adhesion interaction distance to <code>new_value</code>, as a multiple of the cell’s mean equivalent radius. It preserves the repulsion strength and equilibrium cell-cell spacing, by adjusting the adhesion strength.</p></li>
<li><p><strong><code>void set_relative_equilibrium_distance( double new_value )</code></strong> sets the new cell-cell equilibrium spacing or distance to <code>new_value</code>, as a multiple of the cell’s mean equivalent radius. It preserves the repulsion strength and maximum mechanical interaction distance, by adjusting the adhesion strength. Note that this function performs a “sanity check” cap <code>new_value</code> at 2.0.</p></li>
<li><p><strong><code>void set_absolute_equilibrium_distance( Phenotype&amp; phenotype, double new_value )</code></strong> sets the new cell-cell equilibrium spacing or distance to <code>new_value</code>, in absolute units (microns). It requires the cell’s equivalent radius, as given within the supplied <code>phenotype</code> as a multiple of the cell’s mean equivalent radius. It preserves the repulsion strength and maximum mechanical interaction distance, by adjusting the adhesion strength. Note that this function performs a “sanity check” cap <code>new_value</code> at 2 cell radii. Note also that internally, PhysiCell performs physical calculations based upon the multiples of the cell’s current radius. This means that the equilibrium distance will stay the same relative to the cell’s radius, but the absolute (dimensional) equilibrium spacing will vary in time even after setting the value with this function.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Motility">Motility </h2>
<p><code>Motility</code> stores motility parameters and the current speed/direction of motility. It was designed to be sufficiently generic to allow recovery of purely Brownian motion, deterministic taxis, and combinations of these. Here are the main data elements:</p>
<ol>
<li><p><strong><code>bool is_motile</code></strong> is a Boolean variable that can be used to enable/disable cell motility.</p></li>
<li><p><strong><code>double persistence_time</code></strong> is the mean time cell continues at its current speed and direction before re-evaluating and choosing a new motility vector. It is assumed to have units minutes.</p></li>
<li><p><strong><code>double migration_speed</code></strong> is the speed of motility, in the absence of other forces (e.g., cell-cell adhesion). It is assumed to have units of <span class="math inline"><em>μ</em>m/min</span>.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; migration_bias_direction</code></strong> is the 3-D vector giving the cell’s preferred direction of motility for biased Brownian motion. If the user modifies this vector, they must ensure it is a <em>unit vector</em>: <span class="math display">||<code>migration_bias_direction</code>|| = 1.</span></p></li>
<li><p><strong><code>double migration_bias</code></strong> (with a value in [0,1]) sets the degree to which cell motility is biased along <code>migration_bias_direction</code>. If 0, then motion is completely Brownian. If 1, it is completely deterministc along the bias direction.</p></li>
<li><p><strong><code>bool restrict_to_2D</code></strong> is a Boolean variable that is set to <code>true</code> is we are restricting cell motility to 2D.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; motility_vector</code></strong> is the velocity vector for cell motility, based upon the all the variables and parameters defined above. See also Section <a href="#sec:motility_definitions" data-reference-type="ref" data-reference="sec:motility_definitions">11.6.2</a>.</p></li>
</ol>
<p>Here is the class definition:</p>
<pre><code>class Motility
{
 public:
    bool is_motile; 
 
    double persistence_time; 
    double migration_speed;     
    std::vector&lt;double&gt; migration_bias_direction; 
    double migration_bias; 
    bool restrict_to_2D; 
    std::vector&lt;double&gt; motility_vector; 
        
    Motility();      
};</code></pre>
<p>The main parameters are further defined and related in Section <a href="#sec:motility_definitions" data-reference-type="ref" data-reference="sec:motility_definitions">11.6.2</a></p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="member-functions-11">Member functions</h3>
<ol>
<li><p><strong><code>Motility()</code></strong> is the default constructor function. Note that it sets:</p>
<p><code>is_motile = false</code>, <code>update_migration_bias_vector = NULL</code>, and <code>restrict_to_2D = false</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:motility_definitions">Motility definitions</h3>
<p>The direction of (biased random) motility is given by <span class="math display">$$\mathbf{d}_\textrm{mot} = 
\frac{ b \, \mathbf{d}_\textrm{bias} + (1-b) \boldsymbol{\xi} }{ \left|\left|{  b \, \mathbf{d}_\textrm{bias} + (1-b) \boldsymbol{\xi} }\right|\right| }
\label{eq:motility_direction}$$</span> where <span class="math inline"><em>b</em></span> (<code>migration_bias</code>) is the level of bias, <span class="math inline"><strong>ξ</strong></span> is a random unit vector (length 1, uniformly random direction), and <span class="math inline"><strong>d</strong><sub>bias</sub></span> (<code>migration_bias_direction</code>) is the directional bias for motility. See Section <a href="#sec:cell_member_functions" data-reference-type="ref" data-reference="sec:cell_member_functions">9.2</a> for more information on how the <code>Motility</code> class is used when updating a cell’s velocity.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Secretion">Secretion </h2>
<p><code>Secretion</code> collects the cell’s biotransport parameters for interfacing with BioFVM <span class="citation" data-cites="ref:BioFVM"></span>. Its main data elements include:</p>
<ol>
<li><p><strong><code>Microenvironment* pMicroenvironment</code></strong> is a pointer to the correct microenvironment, where substrates have already been declared.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; secretion_rates</code></strong> is a vector of secretion rates for the substrates in the microenvironment.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; uptake_rates</code></strong> is a vector of uptake rates for the substrates in the microenvironment.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; net_export_rates</code></strong> is a vector of net export rates for substrates in the environment, which was added to PhysiCell in Version 1.7.0. It allows more generic secretion models (including both net positive and net negative secretion). Users generally should <em>either</em> use <code>secretion_rates</code> <em>or</em> <code>net_export_rates</code>, but generally not both.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; saturation_densities</code></strong> is a vector of densities at which secretions saturate. See <span class="citation" data-cites="ref:BioFVM"></span>.</p></li>
</ol>
<p>Here is the full class declaration:</p>
<pre><code>class Secretion
{
 private:
 public:
    Microenvironment* pMicroenvironment; 
    
    std::vector&lt;double&gt; secretion_rates; 
    std::vector&lt;double&gt; uptake_rates; 
    std::vector&lt;double&gt; saturation_densities;
    std::vector&lt;double&gt; net_export_rates; 

    Secretion();      

    void sync_to_current_microenvironment( void );      
    void advance( Basic_Agent* pCell, Phenotype&amp; phenotype , double dt ); 
    
    void sync_to_microenvironment( Microenvironment* pNew_Microenvironment );
    
    void set_all_secretion_to_zero( void ); 
    void set_all_uptake_to_zero( void ); 
    void scale_all_secretion_by_factor( double factor ); 
    void scale_all_uptake_by_factor( double factor ); 
};</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="member-functions-12">Member functions</h3>
<ol>
<li><p><strong><code>Secretion()</code></strong> is the default constructor. If a default Microenvironment has already been set in BioFVM, then <code>pMicroenvironment</code> is set to this (otherwise <code>NULL</code>). Thereafter, <code>secretion_rates</code>, <code>uptake_rates</code>, and <code>saturation_densities</code> are resized for consistency with <code>pMicroenvironment</code>, with all values set to 0.0.</p></li>
<li><p><strong><code>void sync_to_current_microenvironment(void)</code></strong> resizes <code>secretion_rates</code>, <code>uptake_rates</code>, <code>net_export_rates</code>, and <code>saturation_densities</code> consistency with <code>pMicroenvironment</code> and sets all vector entries to 0.0.</p></li>
<li><p><strong><code>void sync_to_microenvironment(Microenvironment* pNew_Microenvironment)</code></strong> sets <code>pMicroenvironment = pNew_Microenvironment</code>, resizes <code>secretion_rates</code>, <code>uptake_rates</code>, <code>net_export_rates</code>, and <code>saturation_densities</code> for consistency with <code>pMicroenvironment</code>, and sets all vector entries to 0.0.</p></li>
<li><p><strong><code>void advance( Basic_Agent* pCell, Phenotype&amp; phenotype, double dt)</code></strong> evaluates the<br />
BioFVM secretion/export and uptake functions for this individual cell. Consistency checks with BioFVM (including those from volume changes) are fully automated.</p></li>
<li><p><strong><code>void set_all_secretion_to_zero( void )</code></strong> sets all the secretion and net export rates to zero. (Please note that settings <code>pCell-&gt;is_active = false</code> is the most efficient way to set all secretion and uptake to zero in a cell.)</p></li>
<li><p><strong><code>void set_all_uptake_to_zero( void )</code></strong> sets all the uptake rates to zero. (Please note that settings <code>pCell-&gt;is_active = false</code> is the most efficient way to set all secretion and uptake to zero in a cell.)</p></li>
<li><p><strong><code>void scale_all_secretion_by_factor(double factor)</code></strong> multiplies all the secretion and net export rates by <code>factor</code>.</p></li>
<li><p><strong><code>void scale_all_uptake_by_factor(double factor)</code></strong> multiplies all the uptake rates by <code>factor</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:phenotype_molecular">Molecular</h2>
<p><code>Molecular</code> collects molecular-scale data and models for the cell. As of Version 1.5.0, this structure tracks internalized total substrates (See Section <a href="#sec:BioFVM_internalization_tracking" data-reference-type="ref" data-reference="sec:BioFVM_internalization_tracking">8.6</a>) in the cell after secretion and uptake. It is up to end users to supply an internal function (e.g., as part of the phenotype function) to create internalized substrate (for subsequent secretion) and/or consume internalized substrate (after uptake).</p>
<p>By default, internalized substrate tracking is turned off. See Section <a href="#sec:BioFVM_internalization_tracking" data-reference-type="ref" data-reference="sec:BioFVM_internalization_tracking">8.6</a> to learn how to enable this feature.</p>
<p>The main data elements include:</p>
<ol>
<li><p><strong><code>Microenvironment* pMicroenvironment</code></strong> is a pointer to the correct microenvironment, where substrates have already been declared.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; internalized_total_substrates</code></strong> is a vector of the total net internalized substrates for the cell. (Note that these are totals, not concentrations or densities. To get a density, divide by the cell’s total volume.) This vector’s size and ordering matches the diffusing substrates in the microenvironment.</p>
<p>Note that at cell division, each daughter cell receives half of each internalized substrate.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; fraction_released_at_death</code></strong> is a vector of the total fraction (between 0 and 1) of each substrate that is released back into the microenvironment (at the cell’s location) at the end of death. By default, this is a zero vector. This vector’s size and ordering matches the diffusing substrates in the microenvironment.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; fraction_transferred_when_ingested</code></strong> is a vector of the total fraction (between 0 and 1) of each substrate that is absorbed by any cell that consumes this cell. By default, this is a zero vector. (Note that these are totals, not concentrations or densities. To get a density, divide by the cell’s total volume.) This vector’s size and ordering matches the diffusing substrates in the microenvironment.</p></li>
</ol>
<p>Here is the full class definition:</p>
<pre><code>class Molecular
{
    private:
    public: 
        Microenvironment* pMicroenvironment; 
    
        Molecular(); 
     
        std::vector&lt;double&gt; internalized_total_substrates; 
        std::vector&lt;double&gt; fraction_released_at_death; 
        std::vector&lt;double&gt; fraction_transferred_when_ingested; 
        
        void sync_to_current_microenvironment( void );
        void sync_to_microenvironment( Microenvironment* pNew_Microenvironment );
        void sync_to_cell( Basic_Agent* pCell );        
};</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:molecular_functions">Member functions</h3>
<ol>
<li><p><strong><code>Molecular()</code></strong> is the default constructor. You should never need to call this function.</p></li>
<li><p><strong><code>void sync_to_current_microenvironment( void )</code></strong> syncs this class’s data structures to the microenvironment in <code>pMicroenvironment</code> if it is non-NULL, or sets all to size zero. All values are initially zero.</p></li>
<li><p><strong><code>void sync_to_microenvironment( Microenvironment* pNew_Microenvironment )</code></strong> syncs this class’s data structures to the microenvironment at <code>pNew_Microenvironment</code>. All values are initially zero.</p></li>
<li><p><strong><code>void sync_to_cell( Basic_Agent* pCell )</code></strong> sets the cell’s internal pointers to this class’s data structures.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:Cell_Container">Cell Containers</h1>
<p>PhysiCell uses <code>Cell_Container</code>s to help organize and search for cells within the simulation (spatial) domain, and to accelerate cell-cell mechanics. It is overloaded with much of the core functionality of PhysiCell, so we highly recommend that you <em><strong>avoid direct operations on cell containers!</strong></em> For reference, here is the full class definition:</p>
<pre><code>class Cell_Container : public BioFVM::Agent_Container
{
 private:    
    std::vector&lt;Cell*&gt; cells_ready_to_divide; 
    std::vector&lt;Cell*&gt; cells_ready_to_die;
    int boundary_condition_for_pushed_out_agents;     
    bool initialzed = false;
    
 public:
    BioFVM::Cartesian_Mesh underlying_mesh;
    std::vector&lt;double&gt; max_cell_interactive_distance_in_voxel;
    int num_divisions_in_current_step;
    int num_deaths_in_current_step;

    double last_diffusion_time =0.0; 
    double last_cell_cycle_time = 0.0;
    double last_mechanics_time = 0.0;
    Cell_Container();
    void initialize(double x_start, double x_end, 
        double y_start, double y_end, double z_start, double z_end, 
        double voxel_size);
    void initialize(double x_start, double x_end, 
        double y_start, double y_end, double z_start, double z_end, 
        double dx, double dy, double dz);
    std::vector&lt;std::vector&lt;Cell*&gt; &gt; agent_grid;
    std::vector&lt;std::vector&lt;Cell*&gt; &gt; agents_in_outer_voxels;
    
    void update_all_cells(double t);
    void update_all_cells(double t, double dt);
    void update_all_cells(double t, double phenotype_dt, double mechanics_dt);
    void update_all_cells(double t, double phenotype_dt, double mechanics_dt,
        double diffusion_dt ); 

    void register_agent( Cell* agent );
    void add_agent_to_outer_voxel(Cell* agent);
    void remove_agent(Cell* agent );
    void remove_agent_from_voxel(Cell* agent, int voxel_index);
    void add_agent_to_voxel(Cell* agent, int voxel_index);
    
    void flag_cell_for_division( Cell* pCell ); 
    void flag_cell_for_removal( Cell* pCell ); 
    bool contain_any_cell(int voxel_index);
};</code></pre>
<p>Users may want to use the following function to ensure that the mechanics data structures are set up consistently with BioFVM microenvironment’s domain:</p>
<pre><code>Cell_Container* create_cell_container_for_microenvironment( BioFVM::Microenvironment&amp; m, 
    double mechanics_voxel_size );</code></pre>
<p>Here is an example use:</p>
<pre><code>// Set mechanics voxel size. 
double mechanics_voxel_size = 30; 

// Assume microenvironment is defined above somewhere. 

// Set up the PhysiCell mechanics data structure. 
Cell_Container* cell_container = create_cell_container_for_microenvironment(
    microenvironment, mechanics_voxel_size );</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h1 id="physicell-inputs">PhysiCell Inputs</h1>
<p>As of Version 1.3.0, we began introducing functions to read XML files to initialize PhysiCell options. We will continue expanding these functions over the next few releases.</p>
<h2 id="sec:XML">XML parsing in PhysiCell</h2>
<p>The following functions make use of pugixml <span class="citation" data-cites="ref:pugixml"></span> to parse XML files and extract parameters. Note that in the DOM (document object model), pugixml’s key data structure is the <code>pugi::xml_node</code>, which corresponds roughly to an XML tag. It can have attribute, a data value, parent elements, and child elements.</p>
<p>PhysiCell’s XML parsing is found in <code>./modules/PhysiCell_pugixml.*</code>, and it all is based upon finding XML nodes relative to a supplied parent (pugixml) XML node. Here are the main functions:</p>
<ol>
<li><p><strong><code>pugi::xml_node xml_find_node(pugi::xml_node&amp; parent_node , std::string find_me)</code></strong> returns the first XML child node named <code>find_me</code> under the XML <code>parent_node</code>. For example:</p>
<pre><code>&lt;parent_node&gt;
   &lt;find_me /&gt;
&lt;/parent_node&gt;</code></pre></li>
<li><p><strong><code>std::string xml_get_string_value(pugi::xml_node&amp; parent_node , std::string find_me)</code></strong> returns a string value for the <code>find_me</code> tag within the <code>parent_node</code> parent. For example:</p>
<pre><code>&lt;parent_node&gt;
   &lt;find_me&gt;output32&lt;/find_me&gt; 
&lt;/parent_node&gt;</code></pre></li>
<li><p><strong><code>double xml_get_double_value(pugi::xml_node&amp; parent_node , std::string find_me)</code></strong> returns a double value for the <code>find_me</code> tag within the <code>parent_node</code> parent. For example:</p>
<pre><code>&lt;parent_node&gt;
   &lt;find_me&gt;3.14&lt;/find_me&gt; 
&lt;/parent_node&gt;</code></pre></li>
<li><p><strong><code>double xml_get_int_value(pugi::xml_node&amp; parent_node , std::string find_me)</code></strong> returns an integer value for the <code>find_me</code> tag within the <code>parent_node</code> parent. For example:</p>
<pre><code>&lt;parent_node&gt;
   &lt;find_me&gt;3&lt;/find_me&gt; 
&lt;/parent_node&gt;</code></pre></li>
<li><p><strong><code>double xml_get_bool_value(pugi::xml_node&amp; parent_node , std::string find_me)</code></strong> returns an Boolean value for the <code>find_me</code> tag within the <code>parent_node</code> parent. For example:</p>
<pre><code>&lt;parent_node&gt;
   &lt;find_me&gt;true&lt;/find_me&gt; 
&lt;/parent_node&gt;</code></pre>
<p>Note that Booleans can be represented as 0 and 1, or <code>false</code> and <code>true</code>.</p></li>
<li><p><strong><code>std::string xml_get_my_name( pugi::xml_node node )</code></strong> helps to easily extract the name of an XML node. (e.g., <code>&lt;bob units="none"&gt;</code> returns bob.)</p></li>
<li><p><strong><code>bool xml_get_my_bool_value( pugi::xml_node node )</code></strong> gets the Boolean value of an XML node. (e.g., <code>&lt;bob units="none"&gt;true&lt;/bob&gt;</code> returns true.)</p></li>
<li><p><strong><code>int xml_get_my_int_value( pugi::xml_node node )</code></strong> gets the int value of an XML node. (e.g., <code>&lt;bob units="none"&gt;42&lt;/bob&gt;</code> returns 42.)</p></li>
<li><p><strong><code>int xml_get_my_double_value( pugi::xml_node node )</code></strong> gets the double value of an XML node. (e.g., <code>&lt;bob units="none"&gt;42.03&lt;/bob&gt;</code> returns 42.03.)</p></li>
<li><p><strong><code>std::string xml_get_my_string_value( pugi::xml_node node )</code></strong> gets the string value of an XML node. (e.g., <code>&lt;bob units="none"&gt;is nice&lt;/bob&gt;</code> returns ïs nice.̈)</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:XML_options">Passing XML options to PhysiCell</h2>
<p>PhysiCell 1.3.0 introduced preliminary support for XML configuration files, via <code>./modules/PhysiCell_settings.*</code>. Version 1.4.0 introduced further refinements that are detailed in Sections <a href="#sec:XML_PhysiCell_structure" data-reference-type="ref" data-reference="sec:XML_PhysiCell_structure">13.3</a> and <a href="#sec:XML_user_parameters" data-reference-type="ref" data-reference="sec:XML_user_parameters">13.5</a>. Version 1.6.0 introduced an XML-based specification of the chemical microenvironment. See Section <a href="#sec:XML_microenvironment_setup" data-reference-type="ref" data-reference="sec:XML_microenvironment_setup">13.4</a>.</p>
<p>XML options in PhysiCell work primarily by creating two data structures defined as:</p>
<pre><code>class PhysiCell_Settings
{
 private:
 public:
     // overall 
     double max_time;   

     // units
     std::string time_units; 
     std::string space_units; 
 
     // parallel options 
     int omp_num_threads; 
     
     // save options
     std::string folder; 

     double full_save_interval;  
     bool enable_full_saves; 
     bool enable_legacy_saves; 
     
     double SVG_save_interval; 
     bool enable_SVG_saves; 
     
     PhysiCell_Settings();
     
     void read_from_pugixml( void ); 
};

class PhysiCell_Globals
{
 private:
 public:
     double current_time; 
     double next_full_save_time; 
     double next_SVG_save_time; 
     int full_output_index; 
     int SVG_output_index; 
};</code></pre>
<p>Notice that PhysiCell needs to load an XML configuration file before it can be queried for parameter values. Use:</p>
<p><code>bool load_PhysiCell_config_file( std::string filename );</code></p>
<p>Note that the sample projects allow the user to specify the XML configuration file. For example, if your executable is <code>run_me</code>, and your configuration file is saved in <code>./config/my_config.xml</code>, then use:</p>
<p><code>&gt; ./run_me ./config/my_config.xml</code></p>
<p>Note that PhysiCell will default to <code>./config/PhysiCell_settings.xml</code> in the sample projects if no XML file is supplied:</p>
<p><code>&gt; ./run_me </code></p>
<p>Lastly, we point out that the settings in the XML figuration files and the settings data structures will likely be expanded in the next several PhysiCell releases.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="member-data">Member data</h3>
<ol>
<li><p><strong><code>double max_time</code></strong> is the maximum simulation time.</p></li>
<li><p><strong><code>std::string time_units</code></strong> is the human-readable time units. All PhysiCell functions currently work in minutes, so this should probably be left as <code>min</code> for now!</p></li>
<li><p><strong><code>std::string space_units</code></strong> is the human-readable space units. All PhysiCell functions currently work in <span class="math inline"><em>μ</em>m</span>, so this should probably be left as <code>micron</code> for now!</p></li>
<li><p><strong><code>int omp_num_threads</code></strong> is the number of threads to use for OpenMP parallelization.</p></li>
<li><p><strong><code>std::string folder</code></strong> sets where PhysiCell saves data.</p></li>
<li><p><strong><code>double full_save_interval</code></strong> says how often (in <code>time_units</code>) PhysiCell saves full simulation data (in MultiCellDS format <span class="citation" data-cites="ref:MultiCellDS"></span>).</p></li>
<li><p><strong><code>bool enable_full_saves</code></strong> sets whether PhysiCell saves full simulation data.</p></li>
<li><p><strong><code>bool enable_legacy_saves</code></strong> sets whether PhysiCell saves legacy data and logs for the original demos. If enabled (default: off), it saves at the same frequency as the full saves.</p></li>
<li><p><strong><code>double SVG_save_interval</code></strong> says how often (in <code>time_units</code>) PhysiCell saves SVG cross-sections; see Section <a href="#sec:SVG_functions" data-reference-type="ref" data-reference="sec:SVG_functions">14.1.1</a>.</p></li>
<li><p><strong><code>bool enable_SVG_saves</code></strong> sets whether PhysiCell saves SVG snapshots.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="member-functions-13">Member functions</h3>
<ol>
<li><p><strong><code>void read_from_pugixml( void )</code></strong> initializes the member data based upon the DOM that has previously been loaded with <code>load_PhysiCell_config_file</code>.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:XML_PhysiCell_structure">Structure of PhysiCell XML parameter files</h2>
<p>PhysiCell’s XML files look like this (as of Version 1.6.0); they are subject to extension.</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;user_details /&gt;

&lt;PhysiCell_settings version=&quot;devel-version&quot;&gt;
   &lt;domain&gt;
      &lt;x_min&gt;-1000&lt;/x_min&gt;
      &lt;x_max&gt;1000&lt;/x_max&gt;
      &lt;y_min&gt;-1000&lt;/y_min&gt;
      &lt;y_max&gt;1000&lt;/y_max&gt;
      &lt;z_min&gt;-10&lt;/z_min&gt;
      &lt;z_max&gt;10&lt;/z_max&gt;
      &lt;dx&gt;20&lt;/dx&gt;
      &lt;dy&gt;20&lt;/dy&gt;
      &lt;dz&gt;20&lt;/dz&gt;
      &lt;use_2D&gt;true&lt;/use_2D&gt;
   &lt;/domain&gt;
   
   &lt;overall&gt;
      &lt;max_time units=&quot;min&quot;&gt;7200&lt;/max_time&gt;  
      &lt;time_units&gt;min&lt;/time_units&gt;
      &lt;space_units&gt;micron&lt;/space_units&gt;
      
      &lt;dt_diffusion units=&quot;min&quot;&gt;0.01&lt;/dt_diffusion&gt;
      &lt;dt_mechanics units=&quot;min&quot;&gt;0.1&lt;/dt_mechanics&gt;
      &lt;dt_phenotype units=&quot;min&quot;&gt;6&lt;/dt_phenotype&gt;    
   &lt;/overall&gt;
   
   &lt;parallel&gt;
      &lt;omp_num_threads&gt;4&lt;/omp_num_threads&gt;
   &lt;/parallel&gt; 
   
   &lt;save&gt;
      &lt;folder&gt;output&lt;/folder&gt; &lt;!-- use . for root --&gt; 

      &lt;full_data&gt;
         &lt;interval units=&quot;min&quot;&gt;60&lt;/interval&gt;
         &lt;enable&gt;true&lt;/enable&gt;
      &lt;/full_data&gt;
      
      &lt;SVG&gt;
         &lt;interval units=&quot;min&quot;&gt;42.0&lt;/interval&gt;
         &lt;enable&gt;true&lt;/enable&gt;
      &lt;/SVG&gt;
      
      &lt;legacy_data&gt;
         &lt;enable&gt;false&lt;/enable&gt;
      &lt;/legacy_data&gt;
   &lt;/save&gt;
   
   &lt;microenvironment_setup&gt;
   &lt;/microenvironment_setup&gt;
   
   &lt;user_parameters&gt;
   &lt;/user_parameters&gt;

&lt;/PhysiCell_settings&gt;</code></pre>
<p>The main groupings of settings are:</p>
<ol>
<li><p><strong><code>domain</code></strong> stores settings on the simulation domain size. As of Version 1.4.0, all PhysiCell sample projects parse this section and set hte simulation size accordingly, although most override the <code>use_2D</code> setting due to 2D/3D specific tissue initializations.</p></li>
<li><p><strong><code>overall</code></strong> stores overall simulation settings, like units and maximum simulation time.</p></li>
<li><p><strong><code>parallel</code></strong> stores OpenMP options.</p></li>
<li><p><strong><code>save</code></strong> stores settings for where and how often data are saved.</p></li>
<li><p><strong><code>microenvironment_setup</code></strong> specifies the chemical substrates in the microenvironment, including their diffusion and decay parameters and initial and boundary conditions. This block also sets some options for the diffusion solvers in BioFVM. See <a href="#sec:XML_microenvironment_setup" data-reference-type="ref" data-reference="sec:XML_microenvironment_setup">13.4</a> for more details.</p></li>
<li><p><strong><code>user_parameters</code></strong> stores user-defined parameters, specific to their simulation. See <a href="#sec:XML_user_parameters" data-reference-type="ref" data-reference="sec:XML_user_parameters">13.5</a> for more details.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:XML_microenvironment_setup">Microenvironment Setup</h2>
<p>As of Version 1.6.0, PhysiCell users can fully define the chemical microenvironment by simple modifications to the XML configuration file. (See Section <a href="#sec:BioFVM" data-reference-type="ref" data-reference="sec:BioFVM">8</a> to learn more about the BioFVM chemical microenvironment.) In Section <a href="#sec:XML_microenvironment_setup_XML_structure" data-reference-type="ref" data-reference="sec:XML_microenvironment_setup_XML_structure">13.4.1</a>, we show how to structure this block of XML.</p>
<p>A detailed tutorial on these parameters is provided at:</p>
<div class="center">
<p><a href="http://mathcancer.org/blog/setting-up-the-physicell-microenvironment-with-xml">http://mathcancer.org/blog/setting-up-the-physicell-microenvironment-with-xml</a></p>
</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:XML_microenvironment_setup_XML_structure">Defining chemical microenvironmental substrates as XML</h3>
<p>The <strong><code>microenvironment_setup</code></strong> section of the XML configuration file defines a number of <code>variable</code>s, followed by <code>options</code>:</p>
<pre><code>&lt;microenvironment_setup&gt;
   &lt;variable /&gt;
   &lt;/variable /&gt;
 
   &lt;options /&gt;
&lt;/microenvironment_setup&gt;</code></pre>
<p>Each chemical substrate is defined in a <strong><code>variable</code></strong> of the following form:</p>
<pre><code>&lt;variable name=&quot;NAME&quot; units=&quot;UNITS&quot; ID=&quot;#&quot;&gt;
   &lt;physical_parameter_set&gt;
      &lt;diffusion_coefficient units=&quot;LENGTH_UNITS^2/TIME_UNITS&quot;&gt;VALUE1
         &lt;/diffusion_coefficient&gt;
      &lt;decay_rate units=&quot;1/TIME_UNITS&quot;&gt;VALUE2&lt;/decay_rate&gt;  
   &lt;/physical_parameter_set&gt;
   &lt;initial_condition units=&quot;UNITS&quot;&gt;VALUE3&lt;/initial_condition&gt;
   &lt;Dirichlet_boundary_condition units=&quot;UNITS&quot; enabled=&quot;true&quot;&gt;VALUE4
      &lt;/Dirichlet_boundary_condition&gt;
      &lt;Dirichlet_options&gt;
         &lt;boundary_value ID=&quot;VALUE5&quot; enabled=&quot;false&quot;&gt;VALUE6&lt;/boundary&gt;
         &lt;!-- ... and so forth --&gt;
      &lt;/Dirichlet_options&gt;
&lt;/variable&gt;</code></pre>
<p>Each <strong><code>variable</code></strong> has the following attributes:</p>
<ul>
<li><p><strong><code>name</code></strong> is the name of the substrate. Specifying this is necessary to allow you to search for that substrate within PhysiCell applications. (See Section <a href="#sec:sample_microenvironment" data-reference-type="ref" data-reference="sec:sample_microenvironment">8.3</a>).</p></li>
<li><p><strong><code>units</code></strong> gives the physical units of the substrate density or concentration. These could very well be “dimensionless.” PhysiCell does not actively enforce or convert units, but specifying the units may help prevent errors in your work.</p></li>
<li><p><strong><code>ID</code></strong> is a unique integer index to allow cross-referencing your substrate. These should be sequential and start counting at zero.</p></li>
</ul>
<p><strong><code>variable</code></strong> has several sub-elements, which must all be present:</p>
<ul>
<li><p><strong><code>physical_parameter_set</code></strong> to indicate physical characteristics of the substrate. (The structure is chosen for compatibilty with MultiCellDS <span class="citation" data-cites="ref:MultiCellDS"></span>.) It contains:</p>
<ul>
<li><p><strong><code>diffusion_coefficient</code></strong> is the diffusion coefficient (recorded in <code>VALUE1</code>), with units indicated as an attribute. As before, note that PhysiCell does not convert units. Use this recording for your own clarity and to help ensure unit consistency. By default, PhysiCell uses <span class="math inline"><em>μ</em>m</span> for <code>LENGTH_UNITS</code> and minutes for <code>TIME_UNITS</code> throughout its calculations.</p></li>
<li><p><strong><code>decay_rate</code></strong> is the s ubstrate’s background decay rate (recorded in <code>VALUE2</code>), with units indicated as an attribute.</p></li>
</ul></li>
<li><p><strong><code>initial_condition</code></strong> gives the initial condition for the substrate (recorded in <code>VALUE3</code>), applied <em>uniformly</em> throughout the domain. The units are indicated as the <strong><code>units</code></strong> attribute. If your units are self-consistent, they should match UNITS in the <strong><code>variable</code></strong> above.</p></li>
<li><p><strong><code>Dirichlet_boundary_condition</code></strong> gives the boundary value of the substrate (recorded in <code>VALUE4</code>), to be applied uniformly to all simulation boundaries. This condition is only applied if the attribute <strong><code>enabled</code></strong> is set to <code>true</code>. If <strong><code>enabled</code></strong> is set to false, then BioFVM will default to a Neuman (no flux) condition for that substrate on the simulation boundary.</p>
<p>The units are indicated as the <strong><code>units</code></strong> attribute. If your units are self-consistent, they should match UNITS in the <strong><code>variable</code></strong> above.</p></li>
<li><p><strong><code>Dirichlet_options</code></strong> is an <em>optional</em> element that allows finer grained control on Dirichlet conditions. If <strong><code>Dirchlet_options</code></strong> is missing, the Dirichlet condition is applied to all or none of the boundaries with equal value (indicated by <code>VALUE4</code>).</p>
<p>If <strong><code>Dirichlet_options</code></strong> is present, any individual boundary can have a separate activated/deacticated state and boundary condition value with a separate <strong><code>boundary_value</code></strong> element. The boundary is specified with the <strong><code>ID</code></strong> attribute, where <code>VALUE5</code> is one of (<code>xmin</code>, <code>xmax</code>, <code>ymin</code>, <code>ymax</code>, <code>zmin</code>, or <code>zmax</code>), and substrate concentration (density) on that boundary is given by <code>VALUE6</code>. Notice that if <code>enabled=false</code>, then the Dirichlet condition is <em>disabled</em> on the indicated boundary, leaving instead a Neumann (zero flux) condition for this substrate on this boundary.</p></li>
</ul>
<p>Next, <strong><code>options</code></strong> helps configure additional code behaviors:</p>
<ul>
<li><p><strong><code>calculate_gradients</code></strong> is set to <code>true</code> if the gradient of each substrate is to be computed at each voxel at each mechanical time step. Enable this if you use chemotaxis anywhere in your model.</p></li>
<li><p><strong><code>track_internalized_substrates</code></strong> is set to <code>true</code> if each individual agent is to track its total amount of internalized substrates (based on mass conservation with cell-based uptake and secretion in the biotransport PDEs). See Sections <a href="#sec:BioFVM_internalization_tracking" data-reference-type="ref" data-reference="sec:BioFVM_internalization_tracking">8.6</a> and <a href="#sec:phenotype_molecular" data-reference-type="ref" data-reference="sec:phenotype_molecular">11.8</a> for more details.</p></li>
<li><p><strong><code>initial_condition</code></strong> is not yet supported, but it will eventually provide a place to indicate pre-computed non-uniform conditions, as saved in an external file. For now, a user can manually overwrite the unifrom initial conditions after calling <code>initialize_microenvironment()</code> (typically in a <code>setup_microenvironment()</code> function).</p></li>
<li><p><strong><code>dirichlet_nodes</code></strong> is not yet supported, but it will eventually provide a place to indicate which voxels in the microenvironment should be Dirichlet nodes, and what the boundary values of the substrates should be in those voxels. As in <strong><code>initial_condition</code></strong>, these will be read from an external file. For now, users can set Dirichlet nodes using the functions in Section <a href="#sec:Dirichlet" data-reference-type="ref" data-reference="sec:Dirichlet">8.4</a>.</p></li>
</ul>
<p>Here is a sample of a microenvironment with three substrates (oxygen, glucose, and signal), where there is a Dirichlet boundary condition for oxygen on all boundaries, a Dirichlet condition for glucose on the bottom z boundary only, and no Dirichlet condition for signal. (Note that all units are in <span class="math inline"><em>μ</em>m</span> and minutes.) Here, we compute all gradients, but do not track internalized substrates.</p>
<pre><code>&lt;microenvironment_setup&gt;
   &lt;variable name=&quot;oxygen&quot; units=&quot;mmHg&quot; ID=&quot;0&quot;&gt;
      &lt;physical_parameter_set&gt;
         &lt;diffusion_coefficient units=&quot;micron^2/min&quot;&gt;100000&lt;/diffusion_coefficient&gt;
         &lt;decay_rate units=&quot;1/min&quot;&gt;0.1&lt;/decay_rate&gt;  
      &lt;/physical_parameter_set&gt;
      &lt;initial_condition units=&quot;mmHg&quot;&gt;60&lt;/initial_condition&gt;
      &lt;Dirichlet_boundary_condition units=&quot;mmHg&quot; 
        enabled=&quot;true&quot;&gt;38&lt;/Dirichlet_boundary_condition&gt;
   &lt;/variable&gt;
   
   &lt;variable name=&quot;glucose&quot; units=&quot;dimensionless&quot; ID=&quot;1&quot;&gt;
      &lt;physical_parameter_set&gt;
         &lt;diffusion_coefficient units=&quot;micron^2/min&quot;&gt;18000&lt;/diffusion_coefficient&gt;
         &lt;decay_rate units=&quot;1/min&quot;&gt;0.0&lt;/decay_rate&gt;  
      &lt;/physical_parameter_set&gt;
      &lt;initial_condition units=&quot;dimensionless&quot;&gt;1&lt;/initial_condition&gt;
      &lt;Dirichlet_boundary_condition units=&quot;dimensionless&quot;
         enabled=&quot;true&quot;&gt;0&lt;/Dirichlet_boundary_condition&gt;
      &lt;Dirichlet_options&gt;
         &lt;boundary_value ID=&quot;xmin&quot; enabled=&quot;false&quot;&gt;0&lt;/boundary_value&gt;
         &lt;boundary_value ID=&quot;xmax&quot; enabled=&quot;false&quot;&gt;0&lt;/boundary_value&gt;
         &lt;boundary_value ID=&quot;ymin&quot; enabled=&quot;false&quot;&gt;0&lt;/boundary_value&gt;
         &lt;boundary_value ID=&quot;ymax&quot; enabled=&quot;false&quot;&gt;0&lt;/boundary_value&gt;
         &lt;boundary_value ID=&quot;zmin&quot; enabled=&quot;true&quot;&gt;1&lt;/boundary_value&gt;
         &lt;boundary_value ID=&quot;zmax&quot; enabled=&quot;false&quot;&gt;0&lt;/boundary_value&gt;
      &lt;/Dirichlet_options&gt;
   &lt;/variable&gt;      

   &lt;variable name=&quot;signal&quot; units=&quot;dimensionless&quot; ID=&quot;2&quot;&gt;
      &lt;physical_parameter_set&gt;
         &lt;diffusion_coefficient units=&quot;micron^2/min&quot;&gt;18000&lt;/diffusion_coefficient&gt;
         &lt;decay_rate units=&quot;1/min&quot;&gt;0.0&lt;/decay_rate&gt;  
      &lt;/physical_parameter_set&gt;
      &lt;initial_condition units=&quot;dimensionless&quot;&gt;1&lt;/initial_condition&gt;
      &lt;Dirichlet_boundary_condition units=&quot;dimensionless&quot;
         enabled=&quot;false&quot;&gt;0&lt;/Dirichlet_boundary_condition&gt;
   &lt;/variable&gt;      

   &lt;options&gt;
      &lt;calculate_gradients&gt;true&lt;/calculate_gradients&gt;
      &lt;track_internalized_substrates_in_each_agent&gt;false
         &lt;/track_internalized_substrates_in_each_agent&gt;
      &lt;!-- not yet supported --&gt; 
      &lt;initial_condition type=&quot;matlab&quot; enabled=&quot;false&quot;&gt;
         &lt;filename&gt;./config/initial.mat&lt;/filename&gt;
      &lt;/initial_condition&gt;
      &lt;!-- not yet supported --&gt; 
      &lt;dirichlet_nodes type=&quot;matlab&quot; enabled=&quot;false&quot;&gt;
         &lt;filename&gt;./config/dirichlet.mat&lt;/filename&gt;
      &lt;/dirichlet_nodes&gt;
   &lt;/options&gt;
&lt;/microenvironment_setup&gt;    </code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:microenvironment_xml_parsing_functions">Key microenvironment parsing functions</h3>
<ul>
<li><p><strong><code>bool setup_microenvironment_from_XML( pugi::xml_node root_node )</code></strong> parses the XML DOM (in the supplied pugixml <code>xml_node</code>) to find the <code>microenvironment_setup</code> node and process the variables and options.</p>
<p>It returns true if successful, and false if not.</p></li>
<li><p><strong><code>bool setup_microenvironment_from_XML( void )</code></strong> calls the prior function using <code>physicell_config_root</code>.</p></li>
</ul>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:XML_user_parameters">User Parameters</h2>
<p>As of Version 1.4.0, PhysiCell supports custom Boolean, integer, double, and string user parameters, which are automatically parsed into PhysiCell into a <code>parameters</code> data structure and available for query throughout a project. In Section <a href="#sec:XML_user_parameters_XML_structure" data-reference-type="ref" data-reference="sec:XML_user_parameters_XML_structure">13.5.1</a>, we show how to structure new user parameters in an XML parameter file. In Section <a href="#sec:XML_user_parameters_reading_them" data-reference-type="ref" data-reference="sec:XML_user_parameters_reading_them">13.5.2</a>, we show how to access them within a project. In section <a href="#sec:XML_user_parameters_data_types" data-reference-type="ref" data-reference="sec:XML_user_parameters_data_types">13.5.3</a>, we formally define the data types.</p>
<p>A detailed tutorial on these parameters is provided at:</p>
<div class="center">
<p><a href="http://www.mathcancer.org/blog/user-parameters-in-physicell/">http://www.mathcancer.org/blog/user-parameters-in-physicell/</a></p>
</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:XML_user_parameters_XML_structure">Adding User Parameters to an XML Configuration File</h3>
<p>In the <code>&lt;user_parameters&gt;</code> section of an XML configuration file, you can add any named parameter with the following syntax:</p>
<pre><code>   &lt;user_parameters&gt;
      &lt;parameter_name type=&quot;TYPE&quot; units=&quot;UNITS&quot;&gt;value&lt;/parameter_name&gt;
   &lt;/user_parameters&gt;</code></pre>
<ul>
<li><p><strong>parameter_name</strong> is the name of the parameter. Note that this cannot begin with a digit.</p></li>
<li><p><strong>type</strong> is the type of parameter. Allowed types are bool (Boolean), int (integer), double (floating point double precision), and string (std::string). Note that if this attribute is not supplied, PhysiCell will attempt to process the parameter as a double.</p></li>
<li><p><strong>units</strong> are the units (default: none). Note that PhysiCell does not convert units, so supplying units here is important communication between users to ensure all are using correct units. By default, PhysiCell works in microns for spatial units and minutes for time units.</p></li>
<li><p><strong>value</strong> is the actual value of the parameter.</p></li>
</ul>
<p>Here is an example <code>&lt;user_parameters&gt;</code> with each of these types of data</p>
<pre><code>   &lt;user_parameters&gt;
      &lt;enable_detailed_model type=&quot;bool&quot; units=&quot;none&quot;&gt;true&lt;/enable_detailed_model&gt;
      &lt;number_of_initial_cells type=&quot;int&quot; units=&quot;none&quot;&gt;42&lt;/number_of_initial_cells&gt;
      &lt;division_rate type=&quot;double&quot; units=&quot;1/min&quot;&gt;0.001&lt;/division_rate&gt;
      &lt;mean_waiting_time type=&quot;double&quot; units=&quot;min&quot;&gt;1.2e2&lt;/mean_waiting_time&gt;
      &lt;mutant_cell_color type=&quot;string&quot; units=&quot;none&quot;&gt;rgb(255,0,0)&lt;/mutant_cell_color&gt;
   &lt;/user_parameters&gt;</code></pre>
<p>PhysiCell reads into a global data structure called <code>parameters</code>. All Boolean parameters are in <code>parameters.bools</code>. All integer parameters are stored in <code>parameters.ints</code>. All double parameters are stored in <code>parameters.doubles</code>. All string parameters are stored in <code>parameters.strings</code>. See <a href="#sec:XML_user_parameters_data_types" data-reference-type="ref" data-reference="sec:XML_user_parameters_data_types">13.5.3</a> for technical details of these structures.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:XML_user_parameters_reading_them">Accessing User Parameters in a Project</h3>
<p>Use the () operator to access the <em>value</em> of a parameter, either by its name (easier) or by its index (faster). For example, to get the value of the <code>mean_waiting_time</code>, use:</p>
<pre><code>parameters.doubles(&quot;mean_waiting_time&quot;)</code></pre>
<p>To find the index of this parameter, and then access by index, use:</p>
<pre><code>int i = parameters.doubles.find_index(&quot;mean_waiting_time&quot;);
parameters.doubles(i); </code></pre>
<p>Use the [] operator to access the <em>full data structure</em> of a parameter, either by its name (easier) or by its index (faster). For example, to get the value of the <code>number_of_initial_cells</code>, use:</p>
<pre><code>Parameter&lt;int&gt; param = parameters.ints[&quot;number_of_initial_cells&quot;];
std::cout &lt;&lt; param.name &lt;&lt; &quot; &quot; &lt;&lt; param.units &lt;&lt; &quot; &quot; &lt;&lt; param.value &lt;&lt; std::endl; 
std::cout &lt;&lt; param &lt;&lt; std::endl; </code></pre>
<p>To find the index of this parameter, and then access by index, use:</p>
<pre><code>int i = parameters.ints.find_index(&quot;mean_waiting_time&quot;);
Parameter&lt;int&gt; param = parameters.ints[i]; 
std::cout &lt;&lt; param.name &lt;&lt; &quot; &quot; &lt;&lt; param.units &lt;&lt; &quot; &quot; &lt;&lt; param.value &lt;&lt; std::endl; 
std::cout &lt;&lt; param &lt;&lt; std::endl; </code></pre>
<p>The usage is similar for Boolean, string, and double parameters.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:XML_user_parameters_data_types">User Parameters Technical Details</h3>
<p>We first define a template class for a <code>Parameter</code>:</p>
<pre><code>template &lt;class T&gt; 
class Parameter
{
 private:
   template &lt;class Y&gt;
   friend std::ostream&amp; operator&lt;&lt;(std::ostream&amp; os, const Parameter&lt;Y&gt;&amp; param); 

 public: 
   std::string name; 
   std::string units; 
   T value; 
   
   Parameter();
   Parameter( std::string my_name ); 
   
   void operator=( T&amp; rhs ); 
   void operator=( T rhs ); 
   void operator=( Parameter&amp; p ); 
};</code></pre>
<p>The supported types <code>T</code> are <code>int</code>, <code>double</code>, <code>bool</code>, and <code>std::string</code>. You can use the assignment operator = to either access the entire parameter or just its value. We also provide user-friendly streaming via the <code>&lt;&lt;</code> overator.</p>
<p>Next, we provide a template class <code>Parameters</code> that bundles a searchable vector of parameters.</p>
<pre><code>template &lt;class T&gt;
class Parameters
{
 private:
   std::unordered_map&lt;std::string,int&gt; name_to_index_map; 
   
   template &lt;class Y&gt;
   friend std::ostream&amp; operator&lt;&lt;( std::ostream&amp; os , const Parameters&lt;Y&gt;&amp; params ); 

 public: 
   Parameters(); 
 
   std::vector&lt; Parameter&lt;T&gt; &gt; parameters; 
   
   void add_parameter( std::string my_name ); 
   void add_parameter( std::string my_name , T my_value ); 
   void add_parameter( std::string my_name , T my_value , std::string my_units ); 
   
   void add_parameter( Parameter&lt;T&gt; param );
   
   int find_index( std::string search_name ); 
   
   // these access the values 
   T&amp; operator()( int i );
   T&amp; operator()( std::string str ); 

   // these access the full, raw parameters 
   Parameter&lt;T&gt;&amp; operator[]( int i );
   Parameter&lt;T&gt;&amp; operator[]( std::string str ); 
   
   int size( void ) const; 
};</code></pre>
<p>As shown in the examples above, use the () operator to access a specific parameter value, and use the [] operator to access a specific full parameter data structure. Use <code>find_index</code> to search for the index of a parameter. We also provide a friendly streaming operation to summarize the parameters.</p>
<p>Lastly, <code>User_Parameters</code> bundles Boolean, integer, double, and string parameters:</p>
<pre><code>class User_Parameters
{
 private:
   friend std::ostream&amp; operator&lt;&lt;( std::ostream&amp; os , const User_Parameters up ); 
 
 public:
   Parameters&lt;bool&gt; bools; 
   Parameters&lt;int&gt; ints; 
   Parameters&lt;double&gt; doubles; 
   Parameters&lt;std::string&gt; strings; 
   
   void read_from_pugixml( pugi::xml_node parent_node );
}; </code></pre>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:Outputs">PhysiCell Outputs </h1>
<p>PhysiCell supports several methods of output, including SVG files (allowing virtual pathology through a fixed cross-section), MultiCellDS digital snapshots (a single-time save file), and other output methods.</p>
<p>Over the next several releases, we plan further improvements to PhysiCell outputs.</p>
<h2 id="sec:Pathology">Virtual Pathology</h2>
<p>PhysiCell can simulate transmitted light microscopy to create virtual H&amp;E (hematoxylin and eosin) images, as well as false-colored images. These images are saved as SVG (scalable vector graphics) files, which allow lossless rescaling of the image. Moreover, because SVG files are a specialized XML, users can change labels and other image aspects long after image processing, using simple text editors.</p>
<p>We also note that the SVG functions provided in PhysiCell (<code>./modules/PhysiCell_SVG.h</code>) can be compiled independently of PhysiCell.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:SVG_functions">SVG functions </h3>
<p>SVG functions (defined in <code>./modules/PhysiCell_SVG.h</code>) provide basic functionality for creating SVG files. In all the functions below, please note that the origin <span class="math inline">(0, 0)</span> in an SVG file is in the upper left corner.</p>
<ol>
<li><p><strong><code>bool Write_SVG_start( std::ostream&amp; os, double width, double height )</code></strong> creates the header information for an SVG file of width <code>width</code>, height <code>height</code>, and writes the stream in <code>os</code>.</p>
<p><u>Example:</u> Starting a <span class="math inline">640 × 480</span> image:</p>
<pre><code>// open the file, write a basic &quot;header&quot;
std::ofstream os( &quot;sample_SVG.svg&quot; , std::ios::out );
Write_SVG_start( os, 640, 480 ); </code></pre></li>
<li><p><strong><code>bool Write_SVG_end( std::ostream&amp; os )</code></strong> writes the end of an SVG file to the stream in <code>os</code>.</p>
<p><u>Example:</u> Starting a <span class="math inline">640 × 480</span> image:</p>
<pre><code>// open the file, write a basic &quot;header&quot;
std::ofstream os( &quot;sample_SVG.svg&quot; , std::ios::out );
Write_SVG_start( os, 640, 480 ); 

// operations on the SVG file

// close and save the file 
Write_SVG_end(os); 
os.close(); </code></pre></li>
<li><p><strong><code>bool Write_SVG_text( std::ostream&amp; os, const char* str, double position_x, double position_y, double font_size, const char* color , const char* font)</code></strong> places the text <code>str</code> at (upper left) position <code>[position_x,position_y]</code> with text height <code>font_size</code>, color <code>color</code>, and font <code>font</code>. It writes to the stream <code>os</code>.</p>
<p><u>Example:</u> Placing a dark red “hello world” at (30,60), with font height 17 and the Arial font.</p>
<pre><code>// open the file, write a basic &quot;header&quot;
std::ofstream os( &quot;sample_SVG.svg&quot; , std::ios::out );
Write_SVG_start( os, 640, 480 ); 

std::string my_text = &quot;Hello world!&quot;; 
std::string my_color = &quot;rgb(128,0,0)&quot;; 
std::string my_font = &quot;Arial&quot;; 

Write_SVG_text( os, my_text.c_str(), 30, 60, 17, my_color.c_str(), 
    my_font.c_str() ); 

// close and save the file 
Write_SVG_end(os); 
os.close(); </code></pre></li>
<li><p><strong><code>bool Write_SVG_circle( std::ostream&amp; os, double center_x, double center_y, double radius, double stroke_size, std::string stroke_color, std::string fill_color )</code></strong> places a circle with center at <code>[center_x,center_y]</code> and radius <code>radius</code>. The circle is filled with color <code>fill_color</code>, and an outline of thickness <code>stroke_size</code> and color <code>stroke_color</code>. It writes to the stream <code>os</code>.</p>
<p><u>Example:</u> Placing a cyan circle with black outline at (100,90), with radius 8.6, and outline width 1.</p>
<pre><code>// open the file, write a basic &quot;header&quot;
std::ofstream os( &quot;sample_SVG.svg&quot; , std::ios::out );
Write_SVG_start( os, 640, 480 ); 

std::string my_fill_color = &quot;rgb(0,255,255)&quot;; 
std::string my_outline_color = &quot;black&quot;; 

Write_SVG_circle(os,100,90,8.6,1,my_outline_color.c_str(),my_fill_color.c_str()); 

// close and save the file 
Write_SVG_end(os); 
os.close(); </code></pre></li>
<li><p><strong><code>bool Write_SVG_rect( std::ostream&amp; os, double UL_corner_x, double UL_corner_y, double width, double height, double stroke_size, std::string stroke_color , std::string fill_color )</code></strong> places a rectangle with upper-left corner <code>[UL_corner_x,UL_corner_y]</code>, width <code>width</code>, height <code>height</code>, filled with color <code>fill_color</code>, and outlined with color <code>stroke_color</code> and line thickness <code>stroke_size</code>. It writes to the stream <code>os</code>.</p>
<p><u>Example:</u> Placing a black border with no fill around the SVG image.</p>
<pre><code>// open the file, write a basic &quot;header&quot;
std::ofstream os( &quot;sample_SVG.svg&quot; , std::ios::out );
Write_SVG_start( os, 640, 480 ); 

std::string my_fill_color = &quot;none&quot;; 
std::string my_outline_color = &quot;black&quot;; 

Write_SVG_rect(OS,0,0,640,480,1,my_outline_color.c_str(),my_fill_color.c_str());  
 
// close and save the file 
Write_SVG_end(os); 
os.close(); </code></pre></li>
<li><p><strong><code>bool Write_SVG_line( std::ostream&amp; os, double start_x, double start_y, double end_x, double end_y, double thickness, std::string stroke_color )</code></strong> draws a line with color <code>stroke_color</code> and thickness <code>thickness</code> from <code>[start_x,start_y]</code> to <code>[end_x,end_y]</code>. It writes to the stream <code>os</code>.</p>
<p><u>Example:</u> Placing a thin dark blue line from (0,0) to (640,480).</p>
<pre><code>// open the file, write a basic &quot;header&quot;
std::ofstream os( &quot;sample_SVG.svg&quot; , std::ios::out );
Write_SVG_start( os, 640, 480 ); 

std::string my_stroke_color = &quot;rgb(0,0,64)&quot;; 

Write_SVG_line(os,0,0,640,480,1.5,my_stroke_color.c_str()); 
 
// close and save the file 
Write_SVG_end(os); 
os.close(); </code></pre></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Pathology_functions">Pathology functions </h3>
<p>PhysiCell can create fast virtual pathology images through a cross section. Here are the main functions:</p>
<ol>
<li><p><strong><code>void SVG_plot( std::string filename , Microenvironment&amp; M, double z_slice, double time, std::vector&lt;std::string&gt; (*cell_coloring_function)(Cell*) )</code></strong> creates an SVG<br />
plot through <span class="math inline"><em>z</em> = <code>z_slice</code></span>, using the coloring function <code>cell_coloring_function</code> (See Section <a href="#sec:Pathology_Coloring" data-reference-type="ref" data-reference="sec:Pathology_Coloring">14.1.3</a>), with labeling for time <code>time</code>, in the microenvironment <code>M</code>, saved to <code>filename</code>.</p>
<p>This function checks all cells for intersection with the plane through <span class="math inline"><em>z</em> = <code>z_slice</code></span>, and plots the intersecting part of the cell cytoplasm and nucleus (using circular approximations). In the plot, 1 pixel is 1 <span class="math inline"><em>μ</em>m</span>.</p>
<p><u>Example:</u> H&amp;E plot through <span class="math inline"><em>z</em> = 0<em>μ</em>m</span>, followed by a false-colored Ki-67 plot through <span class="math inline"><em>z</em> = 10<em>μ</em>m</span>:</p>
<pre><code>SVG_plot( &quot;initial_HE.svg&quot; , microenvironment, 0.0 , t, 
    hematoxylin_and_eosin_cell_coloring );
SVG_plot( &quot;initial_Ki67.svg&quot; , microenvironment, 10.0 , t, 
    false_cell_coloring_Ki67 );</code></pre>
<p>The SVG plotting options are set by <code>PhysiCell_SVG_options</code>, which is discussed further in Section <a href="#sec:SVG_options" data-reference-type="ref" data-reference="sec:SVG_options">16.6</a>.</p></li>
<li><p><strong><code>std::string formatted_minutes_to_DDHHMM( double minutes )</code></strong> creates a nicely formated string (in days, hours, and minutes) based upon <code>minutes</code>. It is used extensively in <code>SVG_plot</code>.</p></li>
<li><p><strong><code>std::vector&lt;double&gt; transmission( std::vector&lt;double&gt;&amp; incoming_light, std::vector&lt;double&gt;&amp; absorb_color, double thickness, double stain )</code></strong> simulates transmission of light of color <code>incoming_light</code> through a tissue of thickness <code>thickness</code>, stained at relative intensity <code>stain</code> (with range from 0 to 1), which absorbs light of color <code>absorb_color</code>. Its output is the transmitted color, as an RGB vector.</p>
<p>We use a Lambert-Beer <span class="citation" data-cites="ref:lambert_beer"></span> light transmission model for each color channel (<code>Red</code>, <code>Green</code>, <code>Blue</code>):</p>
<p><span class="math display">$$\begin{aligned}
\texttt{Transmitted}_\texttt{C} &amp; = &amp; \texttt{Incoming}_\texttt{C} 
\cdot 
\exp\left( 
 -\Bigl( \texttt{thickness} 
\cdot \texttt{stain} \cdot \frac{1}{255.0} \texttt{Absorb}_\texttt{C} \Bigr) \right), 
\nonumber \\
 &amp;&amp; 
 \phantom{ } \hfill 
\texttt{C} \in \left\{ \texttt{Red}, \texttt{Green}, \texttt{Blue} \right\}\end{aligned}$$</span></p>
<p>Note that we use 24-bit color, so red, green, and blue values should vary from 0 to 255. Outputs to SVG files will be rounded to the nearest integer value. This function is available for use in custom coloring functions, and PhysiCell uses it for virtual H&amp;E stains.</p></li>
</ol>
<p>Future releases will include functions to color the background according to data values in the BioFVM microenvironment.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Pathology_Coloring">Cell coloring functions </h3>
<p>PhysiCell’s virtual pathology functions are built upon choosing a coloring function for the cells. A coloring function takes the form:</p>
<pre><code>std::vector&lt;std::string&gt; some_coloring_function( Cell* pCell )</code></pre>
<p>and it returns a vector of four strings: the cytoplasm fill color, cytoplasm outline color, nuclear color, and nuclear outline color.</p>
<p>Colors in SVG can be specified as:</p>
<ol>
<li><p><strong>RGB colors:</strong> Use a string of the form <strong><code> "rgb(R,G,B)"</code></strong>, where <code>R</code>, <code>G</code>, and <code>B</code> are the red, green, and blue values, and they are integers between 0 and 255.</p></li>
<li><p><strong>Standard web colors:</strong> Use a string like <strong><code>"black"</code></strong> or <strong><code>"red"</code></strong>, or use <strong><code>"none"</code></strong> for no color (transparent). See <a href="https://www.w3.org/TR/SVG11/types.html#ColorKeywords">https://www.w3.org/TR/SVG11/types.html#ColorKeywords</a> for a list of valid SVG colors.</p></li>
</ol>
<p>The following cell coloring functions are provided in PhysiCell:</p>
<ol>
<li><p><strong><code>simple_cell_coloring</code></strong> colors the cytoplasm red (255,0,0), the nucleus blue (0,0,255), and all outlines black.</p></li>
<li><p><strong><code>false_cell_coloring_Ki67</code></strong> is recommended for the Ki67_Basic and Ki67_Advanced cycle models. (See Section <a href="#sec:Cycle" data-reference-type="ref" data-reference="sec:Cycle">11.1</a> and Section <a href="#sec:Standard_Models:Cycle" data-reference-type="ref" data-reference="sec:Standard_Models:Cycle">17.1</a>.) Pre-mitotic Ki67+ cells are colored green (0,255,0), with a darker green nucleus (0,125,0). Post-mitotic Ki67+ cells are colored magenta (255,0,255), with a darker magenta nucleus (125,0,125). (In the Ki67_Basic model, all Ki67+ cells are green.) Ki67- cells are colored blue (40,200,255) with a darker blue nucleus (20,100,255).</p>
<p>Apoptotic cells are colored red (255,0,0) with a darker red nucleus (125,0,0). Necrotic cells are colored brown (250,138,38) with a darker brown nucleus (139,69,19). All outlines are black.</p></li>
<li><p><strong><code>false_cell_coloring_live_dead</code></strong> colors live cells green, apoptotic cells red, and necrotic cells brown, with colors defined as the Ki67 coloring function. All outlines are black.</p></li>
<li><p><strong><code>hematoxylin_and_eosin_cell_coloring</code></strong> colors the cytoplasm by first using the <code>transmission</code> function, with white (255,255,255) incoming light, an eosin absorb color (2.55,33.15,2.55) <span class="citation" data-cites="ref:H_and_E"></span>, a thickness of 20, and a stain intensity given by <span class="math display">$$\texttt{stain} = 
 \frac{ \texttt{pCell-&gt;phenotype.volume.cytoplasmic\_solid} }
 { \texttt{pCell-&gt;phenotype.volume.cytoplasmic} + 10^{-10} },$$</span> which approximates the process of staining cytoplasmic solids with eosin, and the water fraction remaining unstained. The result of this simulated transmission is then fed back through the <code>transmission</code> function (as the incoming light color), with an hematoxylin absorb color (49.90,51.00,20.40) <span class="citation" data-cites="ref:H_and_E"></span>, a thickness of 20, and a stain intensity given by <span class="math display"><code>stain</code> = <code>pCell-&gt;phenotype.volume.calcified_fraction</code></span> which approximates the process of staining calcified cytoplasmic solids with hematoxylin.</p>
<p>The nucleus is colored by virtual hematoxylin staining, with incoming light color white (255,255,255), hematoxylin absorb color (49.90,51.00,20.40) <span class="citation" data-cites="ref:H_and_E"></span>, and a stain intensity given by <span class="math display">$$\texttt{stain} = 
 \frac{ \texttt{pCell-&gt;phenotype.volume.nuclear\_solid} }
 { \texttt{pCell-&gt;phenotype.volume.nuclear} + 10^{-10} },$$</span> which approximates the process of staining nuclear solids with hematoxylin, and the water fraction remaining unstained.</p>
<p>All outlines match the corresponding fill colors.</p></li>
<li><p><strong><code>false_cell_coloring_cycling_quiescent</code></strong> colors quiescent and cycling cells as Blue and Green, respectively, for use in the <code>cycling_quiescent</code> cell cycle model.</p></li>
<li><p><strong><code>false_cell_coloring_cytometry</code></strong> supports all the various flow cytometry-based cell cycle models. As other coloring funcitons, apoptotic cells are red, and necrotic cells are brown.</p>
<p>G0/G1 cells, or G1 cells, are colored light blue. (0,80,255).<br />
G0 cells are colored pale blue . (40,200,255).<br />
S cells are colored magenta. (255,0,255).<br />
G2 cells are colored yellow. (255,255,0).<br />
G2/M and M cells are colored green. (0,255,0).</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="examples-of-custom-cell-coloring-functions">Examples of custom cell coloring functions</h3>
<h4 id="example-black-nucleus-and-oxygen-based-cytoplasmic-coloring">Example: Black nucleus and oxygen-based cytoplasmic coloring</h4>
<pre><code>std::vector&lt;std::string&gt; oxygen_coloring( Cell* pCell )
{
    std::vector&lt; std::string &gt; output( 4 , &quot;black&quot; ); 
    
    // nucleus and both outlines are already black. 

    // cytoplasm color 

    // first, get the oxygenation 
    
    // determine the o2 index the first time the function is run. 
    static int o2_index = microenvironment.find_density_index( &quot;oxygen&quot; ); 

    // sample the microenvironment at the cell&#39;s locaiton 
    double o2 = pCell-&gt;nearest_density_vector()[o2_index]; 

    // set the o2 max scale by the cell&#39;s parameters. 
    static double max_o2 = pCell-&gt;parameters.o2_proliferation_saturation;  

    // O2 goes from blue (anoxic, 0 mmHg) to red (fully oxygenated). 
    int color = (int) round( o2 * 255.0 / max_o2 ); 
    char szTempString [128]; 
    sprintf( szTempString , &quot;rgb(%u,0,%u)&quot;, color, 255-color ); 
    output[0].assign( szTempString ); 

    return output; 
}</code></pre>
<h4 id="example-simulated-immunohistochemistry-with-dab-and-a-hematoxylin-counterstain">Example: Simulated immunohistochemistry with DAB and a hematoxylin counterstain</h4>
<p>As in H&amp;E, we assume that hematoxylin stains all nuclear solids, and here we assume that it stains cytoplasmic solids at 10% of the nuclear intensity. We assume that DAB stains a nuclear protein (in custom data). Based on these virtual stains, we use simulated light transmission.</p>
<p>For reference, we use a DAB absorb color of (25.50,53.55,73.95) <span class="citation" data-cites="ref:H_and_E"></span>.</p>
<pre><code>std::vector&lt;std::string&gt; nuclear_immunostain( Cell* pCell )
{
    std::vector&lt; std::string &gt; output( 4 , &quot;black&quot; ); 
 
    // absorb colors 
    static std::vector&lt;double&gt; hematoxylin_absorb = {45.90,51.00,20.40};
    static std::vector&lt;double&gt; DAB_absorb = {25.50,53.55,73.95};
 
    // cytoplasm colors 
    double solid_fraction = 1.0 - pCell-&gt;phenotype.fluid_fraction; 
    double cyto_stain_intensity = 0.1 * solid_fraction; 
  
    std::vector&lt;double&gt; = color( 3, 255.0 ); // start with white light 
    color = transmission(color,hematoxylin_absorb,20,cyto_stain_intensity);  
 
    char szTempString [128]; 
    sprintf( szTempString , &quot;rgb(%u,%u,%u)&quot;, 
        (int)round(color[0]), (int)round(color[1]), (int)round(color[2]) ); 
    output[0].assign( szTempString ); 
    output[1].assign( szTempString ); 
 
    // nuclear colors 

    // determine the index of the nuclear protein (assumed between 0 and 1)
    static int protein_index = 
        pCell-&gt;custom_data.find_variable_index( &quot;nuclear_protein&quot; ); 
    double nuclear_DAB_stain_intensity = pCell-&gt;custom_data[protein_index]; 
    double nuclear_H_stain_intensity = solid_fraction; 

    color = {255.0,255.0,255.0}; 
    color = transmission(color,hematoxylin_absorb,20,nuclear_H_stain_intensity);
    color = transmission(color,DAB_absorb,20,nuclear_DAB_stain_intensity);
 
    sprintf( szTempString , &quot;rgb(%u,%u,%u)&quot;, 
        (int)round(color[0]), (int)round(color[1]), (int)round(color[2]) ); 
    output[2].assign( szTempString ); 
    output[3].assign( szTempString ); 
 
    return output; 
}</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h2 id="multicellds-digital-simulation-snapshots">MultiCellDS digital simulation snapshots </h2>
<p>PhysiCell saves its data as specialized MultiCellDS digital snapshots <span class="citation" data-cites="ref:MultiCellDS"></span>. These snapshots save key metadata (See Section <a href="#sec:MultiCellDS_Options" data-reference-type="ref" data-reference="sec:MultiCellDS_Options">16.5</a>), the microenvironment, and a compact cell readout in an XML file. See <span class="citation" data-cites="ref:MultiCellDS"></span> and <a href="http://multicellds.org/Standards.php">http://multicellds.org/Standards.php</a> for detailed information on the data standard.</p>
<p>To save a MultiCellDS simulation snapshot, use:</p>
<p><strong><code>void save_PhysiCell_to_MultiCellDS_xml_pugi( std::string filename_base, Microenvironment&amp; M , double current_simulation_time);</code></strong><br />
Here, the <code>filebase</code> determines how all the snapshot sub-files will be named: <code>filebase.xml</code>, <code>filebase_cells.mat</code>, <code>filebase_mesh0.mat</code>, etc.</p>
<p><u>Example:</u></p>
<pre><code>double t = 0.0;
double dt = 0.01; 
double t_max = 30.0 * 24.0 * 60.0; // 30 days 
double tolerance = 0.01 * dt; 

// other initialization code 

// save the initial data 
save_PhysiCell_to_MultiCellDS_xml_pugi( &quot;initial&quot; , microenvironment , t ); 

double next_save_time = t; 
double save_interval = 60.0; // save every 60 minutes 
output_index = 0; 

while( t &lt; t_max + tolerance )
{
    // save if it&#39;s time
    
    if( fabs( t - next_save_time ) &lt; tolerance )
    {
        // make an appropriate file name 
    
        char filename[1024]; 
        sprintf( filename , &quot;output%08u&quot; , output_index ); 
        
        // save 

        save_PhysiCell_to_MultiCellDS_xml_pugi( filename , microenvironment , t ); 

        next_save_time += save_interval; 
        output_index++; 
    }

    // more simulation steps 

    t += dt; 
}</code></pre>
<p>Here is the overall structure of PhysiCell snapshot</p>
<ol>
<li><p>XML headers in the <code>&lt;XML&gt;</code> tag.</p></li>
<li><p>MultiCellDS tag, indicating a digital simulation snapshot:<br />
<code>&lt;MultiCellDS version="0.5" type="snapshot/simulation"&gt;</code>.</p>
<ol>
<li><p>Metadata in a <code>&lt;metadata&gt;</code> tag, including simulation provenance (who ran it, with what software, citation information, etc.), and other notable elements including:</p>
<ol>
<li><p>The current simulation time, saved in a tag like<br />
<code>&lt;current_time units="min"&gt;0.000000&lt;/current_time&gt;</code>.</p></li>
</ol></li>
<li><p>The BioFVM microenvironment, in a <code>&lt;microenvironment&gt;</code> tag structured as:</p>
<ol>
<li><p><code>&lt;domain&gt;</code> (MultiCellDS can support multiple domains, although we only use one.)</p>
<ol>
<li><p><code>&lt;mesh&gt;</code> describes the BioFVM mesh. The spatial units are given as an XML attribute of this element. Here is the overall (truncated) structure</p>
<pre><code>&lt;mesh type=&quot;Cartesian&quot; uniform=&quot;true&quot; regular=&quot;true&quot; units=&quot;micron&quot;&gt;
    &lt;bounding_box type=&quot;axis-aligned&quot; units=&quot;micron&quot; /&gt;
    &lt;x_coordinates delimiter=&quot; &quot; /&gt;
    &lt;y_coordinates delimiter=&quot; &quot; /&gt;
    &lt;z_coordinates delimiter=&quot; &quot; /&gt;
    &lt;voxels type=&quot;matlab&quot;&gt;
        &lt;filename&gt;initial_mesh0.mat&lt;/filename&gt; &lt;!-- compact storage --&gt;
    &lt;/voxels&gt;
&lt;/mesh&gt;</code></pre>
<p>The voxel information (in this case, in <code>initial_mesh0.mat</code>) is stored with one voxel per column. The first three rows give the x-, y-, and z-coordinates of each voxel’s center, respectively. The fourth row gives each voxel’s volume.</p></li>
<li><p><code>&lt;variables&gt;</code> gives a list of variables, including the name (XML attributes), units (XML attributes), and some physical parameters. Here is a (truncated) example:</p>
<pre><code>&lt;variables&gt;
    &lt;variable name=&quot;oxygen&quot; units=&quot;mmHg&quot; ID=&quot;0&quot;&gt;
        &lt;physical_parameter_set&gt;
            &lt;conditions /&gt;
            &lt;diffusion_coefficient units=&quot;micron^2/min&quot; /&gt;
            &lt;decay_rate units=&quot;1/min&quot; /&gt;
        &lt;/physical_parameter_set&gt;
    &lt;/variable&gt;
&lt;/variables&gt;</code></pre></li>
<li><p>Microenvironment data, typically stored compactly in a MATLAB file, like this:</p>
<pre><code>&lt;data type=&quot;matlab&quot;&gt;
    &lt;filename&gt;initial_microenvironment0.mat&lt;/filename&gt;
&lt;/data&gt;</code></pre>
<p>The data file (here, <code>initialize_microenvironment0.mat</code>) stores the microenvironment in one column per voxel, and if there are <span class="math inline"><em>n</em></span> substrates, <span class="math inline"><em>n</em></span>+3 rows, where rows one to three are the (x,y,z) coordinates of the voxel, and each subsequent row is a variable value (as defined in <code>&lt;variables&gt;</code> above).</p></li>
</ol></li>
<li><p>Cellular information, here in a customized and compact MultiCellDS format:</p>
<pre><code>&lt;cellular_information&gt;
   &lt;cell_populations&gt;
      &lt;cell_population type=&quot;individual&quot;&gt;
         &lt;custom&gt;
            &lt;simplified_data type=&quot;matlab&quot; source=&quot;BioFVM&quot;&gt;
               &lt;filename&gt;initial_cells.mat&lt;/filename&gt;
            &lt;/simplified_data&gt;
            &lt;simplified_data type=&quot;matlab&quot; source=&quot;PhysiCell&quot;&gt;
               &lt;labels&gt;
                  &lt;label index=&quot;0&quot; size=&quot;1&quot;&gt;ID&lt;/label&gt;
                  &lt;label index=&quot;1&quot; size=&quot;3&quot;&gt;position&lt;/label&gt;
                  &lt;label index=&quot;4&quot; size=&quot;1&quot;&gt;total_volume&lt;/label&gt;
                  &lt;label index=&quot;5&quot; size=&quot;1&quot;&gt;cell_type&lt;/label&gt;
                  &lt;label index=&quot;6&quot; size=&quot;1&quot;&gt;cycle_model&lt;/label&gt;
                  &lt;label index=&quot;7&quot; size=&quot;1&quot;&gt;current_phase&lt;/label&gt;
                  &lt;label index=&quot;8&quot; size=&quot;1&quot;&gt;elapsed_time_in_phase&lt;/label&gt;
                  &lt;label index=&quot;9&quot; size=&quot;1&quot;&gt;nuclear_volume&lt;/label&gt;
                  &lt;label index=&quot;10&quot; size=&quot;1&quot;&gt;cytoplasmic_volume&lt;/label&gt;
                  &lt;label index=&quot;11&quot; size=&quot;1&quot;&gt;fluid_fraction&lt;/label&gt;
                  &lt;label index=&quot;12&quot; size=&quot;1&quot;&gt;calcified_fraction&lt;/label&gt;
                  &lt;label index=&quot;13&quot; size=&quot;3&quot;&gt;orientation&lt;/label&gt;
                  &lt;label index=&quot;16&quot; size=&quot;1&quot;&gt;polarity&lt;/label&gt;
               &lt;/labels&gt;
               &lt;filename&gt;initial_cells_physicell.mat&lt;/filename&gt;
            &lt;/simplified_data&gt;
         &lt;/custom&gt;
      &lt;/cell_population&gt;
   &lt;/cell_populations&gt;
&lt;/cellular_information&gt;</code></pre>
<p>In the indicated MATLAB file, each cell is stored in a separate column, with cell-scale data given in separate rows as defined in <code>&lt;labels&gt;</code> above. We anticipate improvements in this MultiCellDS output in future editions, but the data will always be structured as above with labels. We will also always preserve the ordering of the first 17 data elements for compatibility.<br />
In the case above, the first row is the cell ID, the next three rows are the cell (x,y,z) position, the next row is the cell’s (integer) type, the next row gives the cell’s cycle model (as a PhysiCell::constants integer), and so forth.</p></li>
</ol></li>
</ol></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:matlab_data">Reading PhysiCell snapshots in MATLAB</h3>
<p>In the <code>./matlab</code> directory, we include a few MATLAB functions to parse the PhysiCell MultiCellDS XML files and associated .mat files. We recommend copying them to your path, or to the same directory as your data.</p>
<p>Here is an example of loading a snapshot (in MATLAB), plotting a microenvironment variable, and then plotting some cells.</p>
<pre><code>MCDS = read_MultiCellDS_xml( &#39;initial.xml&#39; );
% output looks like this
% Elapsed time is 0.522643 seconds.
% 
% Summary for file initial.xml:
% Voxels: 40000
% Substrates: 1
%   oxygen (mmHg)
% Cells: 21845
%
contour( MCDS.mesh.X , MCDS.mesh.Y, MCDS.continuum_variables(1).data(:,:,1) )
axis ij
axis square
% label using MCDS metadata 
xlabel( sprintf(&#39;x (%s)&#39;, MCDS.metadata.spatial_units) , &#39;fontsize&#39;, 13 )
ylabel( sprintf(&#39;y (%s)&#39;, MCDS.metadata.spatial_units) , &#39;fontsize&#39;, 13 )
% more labeling 
title( sprintf(&#39;%s at time %3.2f %s&#39;, MCDS.continuum_variables(1).name , ...
MCDS.metadata.current_time , MCDS.metadata.time_units) , &#39;fontsize&#39; , 14 );
% add a colorbar, and label 
c = colorbar; 
c.Label.String = sprintf( &#39;%s (%s)&#39;, MCDS.continuum_variables(1).name , ...
MCDS.continuum_variables(1).units ); 
c.FontSize = 13; 
%
%
% Now, plot the cell positions in 3D
figure
plot3( MCDS.discrete_cells.state.position(:,1) , ... 
MCDS.discrete_cells.state.position(:,2), ...
MCDS.discrete_cells.state.position(:,3) , &#39;ko&#39; ); 
% labeling 
axis equal 
xlabel( sprintf(&#39;x (%s)&#39;, MCDS.metadata.spatial_units) , &#39;fontsize&#39;, 13 )
ylabel( sprintf(&#39;y (%s)&#39;, MCDS.metadata.spatial_units) , &#39;fontsize&#39;, 13 )
zlabel( sprintf(&#39;z (%s)&#39;, MCDS.metadata.spatial_units) , &#39;fontsize&#39;, 13 )</code></pre>
<p>We anticipate further refinements to MATLAB plotting, and improvements to importing this data beyond MATLAB. Please also note that the current matlab read script uses the reduced matlab file stored in <code>&lt;simplified_data type="matlab" source="BioFVM"&gt;</code>. Future PhysiCell releases will use the more complete <code>&lt;simplified_data type="matlab" source="PhysiCell"&gt;</code>.</p>
<p>Unfortunately, Octave does not yet ship with xmlread, so the example above will not fully run. You must get the <a href="http://xerces.apache.org/xerces-j/">xerces java binaries</a> and xmlread (in the <a href="https://octave.sourceforge.io/io/index.html">IO</a> octave forge package). There are instructions there on how to get your xerxes JAR files in the path. Please note that xmlread is about one order of magnitude slower on Octave than in Matlab.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="other-outputs">Other outputs </h2>
<p>PhysiCell also has limited POV-ray support (visualization by the open source POV-Ray raytracer), and some additional logging. This will be further documented soon.</p>
<h1 id="sec:Initialization_Functions">Key initialization functions </h1>
<p>The following initialization functions should be called (in this order):</p>
<ol>
<li><p><strong><code>omp_set_num_threads(omp_num_threads);</code></strong> to set the number of threads in the simulation.</p></li>
<li><p><strong><code>SeedRandom();</code></strong> to initialize the random number generator. (It generates a random seed based on the current system time.) You can also use <strong><code>long SeedRandom( long input );</code></strong> to specify the random seed, such as to continue a simulation.</p></li>
<li><p><strong><code>initialize_microenvironment();</code></strong> to initialize the microenvironment, after setting any options in <code>default_microenvironment_options</code>. See Section <a href="#sec:set_up_BioFVM" data-reference-type="ref" data-reference="sec:set_up_BioFVM">8.2</a>.</p></li>
<li><p><strong><code>Cell_Container* cell_container = create_cell_container_for_microenvironment( microenvironment, mechanics_voxel_size );</code></strong>. Note that <code>microenvironment</code> is the default PhysiCell microenvironment. See Section <a href="#sec:Cell_Container" data-reference-type="ref" data-reference="sec:Cell_Container">12</a>.</p></li>
<li><p><strong><code>initialize_default_cell_definition();</code></strong> sets up the default <code>Cell_Definition</code> and makes sure it is self-consistent. It also automatically runs setup functions to create standard cell cycle and death models. Users creating new cell definitions are encouraged to copy the default cell definition and then modify it.</p></li>
</ol>
<p>All these initialization functions are included in the 2-D and 3-D project templates. See Section <a href="#sec:templates" data-reference-type="ref" data-reference="sec:templates">6</a>.</p>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:key_global_data">Key global data structures </h1>
<p>PhysiCell (and BioFVM) have numerous global data structures to help configure options. Here, we detail the most useful of these.</p>
<h2 id="sec:global_strings">Global strings</h2>
<p>The BioFVM and PhysiCell versions and strings can be accessed via</p>
<pre><code>std::string BioFVM_version; 
std::string BioFVM_URL;  
std::string PhysiCell_version; 
std::string PhysiCell_URL; </code></pre>
<h2 id="sec:default_microenvironment">Default microenvironment </h2>
<p>The name of the default microenvironment in PhysiCell is <code>microenvironment</code>, which is declared in <code>./BioFVM/BioFVM_microenvironment.cpp</code>. This structure is initialized with the function</p>
<p><code>initialize_microenvironment()</code></p>
<p>based upon the settings in <code>default_microenvironment_options</code> (of type <code>Microenvironment_Options</code>). Here is the definition of that data structure:</p>
<pre><code>class Microenvironment_Options
{
 private:
 
 public: 
    Microenvironment* pMicroenvironment;
    std::string name; 
 
    std::string time_units; 
    std::string spatial_units; 
    double dx;
    double dy; 
    double dz; 
    
    bool outer_Dirichlet_conditions; 
    std::vector&lt;double&gt; Dirichlet_condition_vector; 
    
    bool simulate_2D; 
    std::vector&lt;double&gt; X_range; 
    std::vector&lt;double&gt; Y_range; 
    std::vector&lt;double&gt; Z_range; 
    
    Microenvironment_Options(); 
    
    bool calculate_gradients; 
};</code></pre>
<p>See Section <a href="#sec:set_up_BioFVM" data-reference-type="ref" data-reference="sec:set_up_BioFVM">8.2</a> for more details on these options.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:cell_definition_default">Default cell definition </h2>
<p>In Section <a href="#sec:Cell_Definition" data-reference-type="ref" data-reference="sec:Cell_Definition">9.4.5</a>, we documented the data structure for a Cell Definition (similar to a MultiCellDS digital cell line <span class="citation" data-cites="ref:MultiCellDS"></span>).</p>
<p>PhysiCell creates a default <code>Cell_Definition</code> called <code>cell_defaults</code>. Once the user calls<br />
<code>initialize_default_cell_definition()</code> (Section <a href="#sec:Initialization_Functions" data-reference-type="ref" data-reference="sec:Initialization_Functions">15</a>), this default definition is set to parameter values for the a generic breast epithelium line (calibrated to MCF-10A).</p>
<ol>
<li><p>It uses the Ki-67 Advanced model. (See Section <a href="#sec:Standard_Models:Ki67_Advanced" data-reference-type="ref" data-reference="sec:Standard_Models:Ki67_Advanced">17.1.3</a>.)</p></li>
<li><p>It defaults to apoptosis and necrosis death models, with parameters for a generic breast epithelium line (calibrated to MCF-10A) as given in <span class="citation" data-cites="ref:PhysiCell"></span>.</p></li>
<li><p>It uses general breast epithelial parameters (calibrated to MCF-10A) for volume, and the standard volume regulation model<br />
<code>standard_volume_update_function</code>. (See Section <a href="#sec:Standard_Models:Volume" data-reference-type="ref" data-reference="sec:Standard_Models:Volume">17.3</a>.)</p></li>
<li><p>It sets the cell to be non-motile.</p></li>
<li><p>It sets the custom rule (<code>custom_cell_rule</code>) to <code>NULL</code> and update phenotype function<br />
(<code>update_phenotype</code>) to <code>update_cell_and_death_parameters_O2_based</code>, so the cell changes its cycle entry rate and necrosis rate according to its local oxygenation conditions. (See Section <a href="#sec:Standard_Models:Microenvironment_Phenotype" data-reference-type="ref" data-reference="sec:Standard_Models:Microenvironment_Phenotype">17.6</a>.)</p></li>
<li><p>It uses the default mechanics model in <span class="citation" data-cites="ref:PhysiCell"></span>, by setting <code>update_velocity</code> equal to<br />
<code>standard_update_cell_velocity</code>. (See Section <a href="#sec:Standard_Models:Velocity" data-reference-type="ref" data-reference="sec:Standard_Models:Velocity">17.4</a>.)</p></li>
</ol>
<p>When <code>create_cell()</code> or the default <code>Cell</code> constructor is called, this default definition is used. (See Section <a href="#sec:other_key_cell_functions" data-reference-type="ref" data-reference="sec:other_key_cell_functions">9.3</a>.)</p>
<p>Users can modify <code>cell_defaults</code> at any time; the changes will only apply to cells created after that point in time.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:All_Cells">A list of all cells</h2>
<p>PhysiCell keeps a list of all current cells in the simulation:</p>
<pre><code>std::vector&lt;Cell*&gt; *all_cells;</code></pre>
<p>It is critical that users <em><span style="color: red"><strong>do not modify this data structure</strong></span></em>, but it is available for peforming an operation on all cells.</p>
<p><u>Example:</u> Dislay the cycle phase of all cells</p>
<pre><code>Cell* pC = NULL; 
for( int i=0; i &lt; (*all_cells).size(); i++ )
{
    pC = (*all_cells)[i]; 
    std::cout &lt;&lt; pC-&gt;ID &lt;&lt; &quot;: &quot; &lt;&lt; pC-&gt;phenotype.cycle.current_phase().name &lt;&lt; std::endl; 
}</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:MultiCellDS_Options">MultiCellDS options </h2>
<p>MultiCellDS embeds program and user metadata each time it saves. You can modify this information. BioFVM (and hence PhysiCell) saves the default metadata in <code>BioFVM_metadata</code> (of type<br />
<code>MultiCellDS_Metadata</code>). Here is the full class definition:</p>
<pre><code>class MultiCellDS_Metadata
{
 private:
 public:
    std::string MultiCellDS_type; 

    Software_Metadata program; 
    Citation_Metadata data_citation; 

    // scientific information  
    std::string spatial_units; 
    std::string time_units;
    std::string runtime_units; 
    double current_time; 
    double current_runtime; 
    
    std::string description; // any optional text -- not implemented 

    MultiCellDS_Metadata();    
    void display_information( std::ostream&amp; os); 
    void sync_to_microenvironment( Microenvironment&amp; M );  
    void restart_runtime( void );  

    void add_to_open_xml_pugi( double current_simulation_time, 
        pugi::xml_document&amp; xml_dom ); 
};</code></pre>
<p>The various member functions are used by BioFVM/PhysiCell when saving a simulation snapshot, and are not needed for users. We define <code>Software_Metadata</code>, <code>Citation_Metadata</code>, and <code>Person_Metadata</code> (currently unused) below. The other metadata elements (<code>spatial_units</code>, etc.) are as expected.</p>
<div class="center">
<hr />
<hr />
</div>
<h3 id="software-metadata">Software metadata</h3>
<pre><code>class Software_Metadata
{
 private:
 public:
    // basic program information   
    std::string program_name; 
    std::string program_version; 
    std::string program_URL;
        
    Person_Metadata creator; 
    Person_Metadata user; 
    Citation_Metadata citation;
    
    Software_Metadata();
    
    void display_information( std::ostream&amp; os ); 
    void insert_in_open_xml_pugi( pugi::xml_node&amp; insert_here );         
};</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="citation-metadata">Citation metadata</h3>
<pre><code>class Citation_Metadata
{
 private:
 public:
    std::string DOI;
    std::string PMID;
    std::string PMCID; 
    std::string text;
    std::string notes; 
    std::string URL; 
    
    Citation_Metadata();  
    void display_information( std::ostream&amp; os );  
    void insert_in_open_xml_pugi( pugi::xml_node&amp; insert_here );    
};</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="person-metadata">Person metadata</h3>
<pre><code>class Person_Metadata
{
 private: 
    bool is_empty; 
 public: 
    std::string type; // author, creator, user, curator 
    std::string surname;
    std::string given_names; 
    std::string email;
    std::string URL; 
    std::string organization; 
    std::string department; 
    std::string ORCID; 
    
    Person_Metadata( ); 
    void display_information( std::ostream&amp; os );          
    void insert_in_open_xml_pugi( pugi::xml_node&amp; insert_here );  
};</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:SVG_options">SVG options </h2>
<p>PhysiCell keeps a simple data structure named <code>PhysiCell_SVG_options</code> (of type<br />
<code>PhysiCell_SVG_options_struct</code>) to easily set SVG plotting options (particularly in digital pathology; see Section <a href="#sec:Pathology" data-reference-type="ref" data-reference="sec:Pathology">14.1</a>). Here is how that data structure is defined (with its default values):</p>
<pre><code>struct PhysiCell_SVG_options_struct
{
    bool plot_nuclei = true; 

    std::string simulation_time_units = &quot;min&quot;;
    std::string mu = &quot;&amp;#956;&quot;;
    std::string simulation_space_units = &quot;&amp;#956;m&quot;;
    
    std::string label_time_units = &quot;days&quot;; 
    
    double font_size = 200; 
    std::string font_color = &quot;black&quot;;
    std::string font = &quot;Arial&quot;;

    double length_bar = 100; 
}; </code></pre>
<p>All plots are performed in the simulation units, so a font of height 200 is 200 <span class="math inline"><em>μ</em>m</span> tall.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:PhysiCell_constants">PhysiCell Constants </h2>
<p>The structure <code>PhysiCell_constants</code> (in <code>./core/PhysiCell_constants.h</code>) defines many standardized constants and integer identifiers. They can be accessed with syntax like this:</p>
<pre><code>std::cout &lt;&lt; &quot;Here is the code for the Ki67 Advanced model: &quot;
          &lt;&lt; PhysiCell_constants::advanced_Ki67_cycle_model &lt;&lt; std::endl; 

Cell* pC = NULL; 
for( int i=0; i &lt; (*all_cells).size(); i++ )
{
   pC = (*all_cells)[i]; 
   if( pC-&gt;phenotype.cycle.current_phase().code == 
       PhysiCell_constants::Ki67_negative )
   {
      std::cout &lt;&lt; &quot;Cell is Ki67 negative&quot; &lt;&lt; std::endl; 
   }
}</code></pre>
<p>Here is the list of all current constants (current as of Version 1.7.0):</p>
<pre><code>class PhysiCell_constants
{
 public:
   static constexpr double pi=3.1415926535897932384626433832795;
   
   static constexpr double cell_removal_threshold_volume = 20; 
   static const int keep_pushed_out_cells_in_outer_voxel=1;
   static const int solid_boundary = 2;
   static const int default_boundary_condition_for_pushed_out_agents 
      = keep_pushed_out_cells_in_outer_voxel;      
   
   static const int deterministic_necrosis = 0;
   static const int stochastic_necrosis = 1;

   static const int mesh_min_x_index=0;
   static const int mesh_min_y_index=1;
   static const int mesh_min_z_index=2;
   static const int mesh_max_x_index=3;
   static const int mesh_max_y_index=4;
   static const int mesh_max_z_index=5;         
   
   static const int mesh_lx_face_index=0;
   static const int mesh_ly_face_index=1;
   static const int mesh_lz_face_index=2;
   static const int mesh_ux_face_index=3;
   static const int mesh_uy_face_index=4;
   static const int mesh_uz_face_index=5;
   
   // currently recognized cell cycle models 
   static const int advanced_Ki67_cycle_model= 0;
   static const int basic_Ki67_cycle_model=1;
   static const int flow_cytometry_cycle_model=2;
   static const int live_apoptotic_cycle_model=3;
   static const int total_cells_cycle_model=4;
   static const int live_cells_cycle_model = 5; 
   static const int flow_cytometry_separated_cycle_model = 6; 
   static const int cycling_quiescent_model = 7; 
   
   // currently recognized death models 
   static const int apoptosis_death_model = 100; 
   static const int necrosis_death_model = 101; 
   static const int autophagy_death_model = 102; 
   
   static const int custom_cycle_model=9999; 
   
   // currently recognized cell cycle and death phases 
   // cycle phases
   static const int Ki67_positive_premitotic=0; 
   static const int Ki67_positive_postmitotic=1; 
   static const int Ki67_positive=2; 
   static const int Ki67_negative=3; 
   static const int G0G1_phase=4;
   static const int G0_phase=5;
   static const int G1_phase=6; 
   static const int G1a_phase=7; 
   static const int G1b_phase=8;
   static const int G1c_phase=9;
   static const int S_phase=10;
   static const int G2M_phase=11;
   static const int G2_phase=12;
   static const int M_phase=13;
   static const int live=14;
   
   static const int G1pm_phase = 15;
   static const int G1ps_phase = 16; 
   
   static const int cycling = 17; 
   static const int quiescent = 18; 
      
   static const int custom_phase = 9999;
   // death phases
   static const int apoptotic=100;
   static const int necrotic_swelling=101;
   static const int necrotic_lysed=102;
   static const int necrotic=103; 
   static const int debris=104; 
};
extern std::string time_units;
extern std::string space_units;
extern double diffusion_dt; 
extern double mechanics_dt;
extern double phenotype_dt;</code></pre>
<p>Notice in particular that cycle models under 100 denote live cells, and cycle models 100 or greater indicate dead cells.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:global_user_parameters">User Parameters</h2>
<p>As detailed in Section <a href="#sec:XML_user_parameters" data-reference-type="ref" data-reference="sec:XML_user_parameters">13.5</a>, PhysiCell has a global <code>User_Parameters</code> data struture called <code>parameters</code>.</p>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:Standard_Models">Standard models </h1>
<p>PhysiCell includes several models for easier out-of-the-box simulation. We document here the underlying mathematics of these models, as also presented in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<h2 id="sec:Standard_Models:Cycle">Cell Cycle Models </h2>
<p>PhysiCell includes several pre-built cell cycle models. More models will be added in future releases.</p>
<h3 id="sec:Standard_Models:Live">Live (<code>live</code>)<br />
code: <code>PhysiCell_constants::live_cells_cycle_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>live</code> with code <code>PhysiCell_constants::live</code>.</p></li>
</ol>
<p>In this model, live cells can divide into two live cells, with birth rate <span class="math inline"><em>b</em></span>. See Fig. <a href="#fig:cycle_model:live" data-reference-type="ref" data-reference="fig:cycle_model:live">[fig:cycle_model:live]</a>. The population-scale model is given by: <span class="math display">$$\frac{dL}{dt} = b L.$$</span> In PhysiCell, the transition rate from the Live state to the Live state is <span class="math display"><code>transition_rate</code>(0, 0) = <em>b</em>.</span> Further details on the <em>biology</em> of this model (including details the placement of daughter cells and changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Standard_Models:Ki67_Basic">Ki-67 Basic (<code>Ki67_basic</code>)<br />
(Code: <code>PhysiCell_constants::basic_Ki67_cycle_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>Ki67-</code> with code <code>PhysiCell_constants::Ki67_negative</code>.</p></li>
<li><p><strong>Phase 1:</strong> Named <code>Ki67+</code> with code <code>PhysiCell_constants::Ki67_positive</code>.</p></li>
</ol>
<p>In this model, Ki67- cells (those staining negative for the cell proliferation marker Ki67) can enter the cell cycle to become Ki67+ cells, at transition rate <span class="math inline"><em>r</em><sub>01</sub></span>. Ki67+ cells divide into two Ki67- cells at rate <span class="math inline"><em>r</em><sub>10</sub></span>. See Fig. <a href="#fig:cycle_model:ki67_basic" data-reference-type="ref" data-reference="fig:cycle_model:ki67_basic">[fig:cycle_model:ki67_basic]</a>. The population-scale model is given by: <span class="math display">$$\begin{aligned}
\frac{d\left[\mathrm{Ki67-}\right]}{dt} &amp; = &amp; -r_{01} \left[\mathrm{Ki67-}\right] + 2 r_{10} \left[\mathrm{Ki67+}\right] \\
\frac{d\left[\mathrm{Ki67+}\right]}{dt} &amp; = &amp;  r_{01} \left[\mathrm{Ki67-}\right] -r_{10} \left[\mathrm{Ki67+}\right] \end{aligned}$$</span> Further details on the <em>biology</em> of this model (including details the placement of daughter cells and changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Standard_Models:Ki67_Advanced">Ki-67 Advanced (<code>Ki67_advanced</code>)<br />
(code: <code>PhysiCell_constants::advanced_Ki67_cycle_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>Ki67-</code> with code <code>PhysiCell_constants::Ki67_negative</code>. This is the default phase of the model.</p></li>
<li><p><strong>Phase 1:</strong> Named <code>Ki67+ (premitotic)</code> with code<br />
<code>PhysiCell_constants::Ki67_positive_premitotic</code>.</p></li>
<li><p><strong>Phase 2:</strong> Named <code>Ki67+ (postmitotic)</code> with code<br />
<code>PhysiCell_constants::Ki67_positive_postmitotic</code>.</p></li>
</ol>
<p>In this model, Ki67- cells (those staining negative for the cell proliferation marker Ki67) can enter the cell cycle to become premitotic Ki67+ cells, at transition rate <span class="math inline"><em>r</em><sub>01</sub></span>. Ki67+ premitotic cells divide into two Ki67+ postmitotic cells at rate <span class="math inline"><em>r</em><sub>12</sub></span>. Postmitotic Ki67+ cells become Ki67- cells at rate <span class="math inline"><em>r</em><sub>20</sub></span>. See Fig. <a href="#fig:cycle_model:ki67_advanced" data-reference-type="ref" data-reference="fig:cycle_model:ki67_advanced">[fig:cycle_model:ki67_advanced]</a>. The population-scale model is given by: <span class="math display">$$\begin{aligned}
\frac{d\left[\mathrm{Ki67-}\right]}{dt} &amp; = &amp; -r_{01} \left[\mathrm{Ki67-}\right] + r_{10} \left[\mathrm{Ki67+ (post)}\right] \\
\frac{d\left[\mathrm{Ki67+ (pre)}\right]}{dt} &amp; = &amp;  r_{01} \left[\mathrm{Ki67-}\right] -r_{12} \left[\mathrm{Ki67+ (pre)}\right] \\
\frac{d\left[\mathrm{Ki67+ (post)}\right]}{dt} &amp; = &amp;  2r_{12} \left[\mathrm{Ki67+ (pre)}\right] -r_{20} \left[\mathrm{Ki67+ (post)}\right] \end{aligned}$$</span> Further details on the <em>biology</em> of this model (including details the placement of daughter cells and changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Standard_Models:Flow_Cytometry">Flow Cytometry (<code>flow_cytometry_cycle_model</code>)<br />
(code: <code>PhysiCell_constants::flow_cytometry_cycle_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>G0G1</code> with code <code>PhysiCell_constants::G0G1_phase</code>. This is the default phase of the model.</p></li>
<li><p><strong>Phase 1:</strong> Named <code>S</code> with code<br />
<code>PhysiCell_constants::S_phase</code>.</p></li>
<li><p><strong>Phase 2:</strong> Named <code>G2M</code> with code<br />
<code>PhysiCell_constants::G2M_phase</code>.</p></li>
</ol>
<p>In this model, <span class="math inline"><em>G</em><sub>0</sub>/<em>G</em><sub>1</sub></span> cells can enter the cell cycle to become <span class="math inline"><em>S</em></span>-phase cells, at transition rate <span class="math inline"><em>r</em><sub>01</sub></span>. <span class="math inline"><em>S</em></span>-phase cells can become <span class="math inline"><em>G</em><sub>2</sub>/<em>M</em></span>-phase cells at rate <span class="math inline"><em>r</em><sub>12</sub></span>. <span class="math inline"><em>G</em><sub>2</sub>/<em>M</em></span>-phase cells can divide into two <span class="math inline"><em>G</em><sub>0</sub>/<em>G</em><sub>1</sub></span> daughter cells at rate <span class="math inline"><em>r</em><sub>20</sub></span>. See Fig. <a href="#fig:cycle_model:flow_cytometry" data-reference-type="ref" data-reference="fig:cycle_model:flow_cytometry">[fig:cycle_model:flow_cytometry]</a>. The population-scale model is given by: <span class="math display">$$\begin{aligned}
\frac{d\left[\mathrm{G0G1}\right]}{dt} &amp; = &amp; -r_{01} \left[\mathrm{G0G1}\right] + 2 r_{20} \left[\mathrm{G2M}\right] \\
\frac{d\left[\mathrm{S}\right]}{dt} &amp; = &amp;  r_{01} \left[\mathrm{G0G1}\right] -r_{12} \left[\mathrm{S}\right] \\
\frac{d\left[\mathrm{G2M}\right]}{dt} &amp; = &amp;  r_{12} \left[\mathrm{S}\right] -r_{20} \left[\mathrm{G2M}\right] \end{aligned}$$</span> Further details on the <em>biology</em> of this model (including details the placement of daughter cells and changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Standard_Models:Flow_Cytometry_Separated">Flow Cytometry Separated (<code>flow_cytometry_separated_cycle_model</code>)<br />
(code: <code>PhysiCell_constants::flow_cytometry_separated_cycle_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>G0G1</code> with code <code>PhysiCell_constants::G0G1_phase</code>. This is the default phase of the model.</p></li>
<li><p><strong>Phase 1:</strong> Named <code>S</code> with code<br />
<code>PhysiCell_constants::S_phase</code>.</p></li>
<li><p><strong>Phase 2:</strong> Named <code>G2</code> with code<br />
<code>PhysiCell_constants::G2_phase</code>.</p></li>
<li><p><strong>Phase 3:</strong> Named <code>M</code> with code<br />
<code>PhysiCell_constants::M_phase</code>.</p></li>
</ol>
<p>In this model, <span class="math inline"><em>G</em><sub>0</sub>/<em>G</em><sub>1</sub></span> cells can enter the cell cycle to become <span class="math inline"><em>S</em></span>-phase cells, at transition rate <span class="math inline"><em>r</em><sub>01</sub></span>. <span class="math inline"><em>S</em></span>-phase cells can become <span class="math inline"><em>G</em><sub>2</sub></span>-phase cells at rate <span class="math inline"><em>r</em><sub>12</sub></span>. <span class="math inline"><em>G</em><sub>2</sub></span>-phase cells can become <span class="math inline"><em>M</em></span>-phase cells at rate <span class="math inline"><em>r</em><sub>23</sub></span>. <span class="math inline"><em>M</em></span>-phase cells can divide into two <span class="math inline"><em>G</em><sub>0</sub>/<em>G</em><sub>1</sub></span> daughter cells at rate <span class="math inline"><em>r</em><sub>30</sub></span>. See Fig. <a href="#fig:cycle_model:flow_cytometry_separated" data-reference-type="ref" data-reference="fig:cycle_model:flow_cytometry_separated">[fig:cycle_model:flow_cytometry_separated]</a>. The population-scale model is given by: <span class="math display">$$\begin{aligned}
\frac{d\left[\mathrm{G0G1}\right]}{dt} &amp; = &amp; -r_{01} \left[\mathrm{G0G1}\right] + 2 r_{30} \left[\mathrm{M}\right] \\
\frac{d\left[\mathrm{S}\right]}{dt} &amp; = &amp;  r_{01} \left[\mathrm{G0G1}\right] -r_{12} \left[\mathrm{S}\right] \\
\frac{d\left[\mathrm{G2}\right]}{dt} &amp; = &amp;  r_{12} \left[\mathrm{S}\right] -r_{23} \left[\mathrm{G2}\right] \\
\frac{d\left[\mathrm{M}\right]}{dt} &amp; = &amp;  r_{23} \left[\mathrm{G2}\right] -r_{30} \left[\mathrm{M}\right] \end{aligned}$$</span> Further details on the <em>biology</em> of this model (including details the placement of daughter cells and changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Standard_Models:cycling_quiescent">Cycling-Quiescent (<code>cycling_quiescent</code>)<br />
(Code: <code>PhysiCell_constants::cycling_quiescent_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>Quiescent</code> with code <code>PhysiCell_constants::quiescent</code>.</p></li>
<li><p><strong>Phase 1:</strong> Named <code>Cycling</code> with code <code>PhysiCell_constants::cycling</code>.</p></li>
</ol>
<p>In this model, Quiescent cells can enter the cell cycle to become Cycling cells, at transition rate <span class="math inline"><em>r</em><sub>01</sub></span>. Cycling cells divide into two Quiescent cells at rate <span class="math inline"><em>r</em><sub>10</sub></span>. See Fig. <a href="#fig:cycle_model:cycling_quiescent" data-reference-type="ref" data-reference="fig:cycle_model:cycling_quiescent">[fig:cycle_model:cycling_quiescent]</a>. The population-scale model is given by: <span class="math display">$$\begin{aligned}
\frac{d\left[\mathrm{Quiescent}\right]}{dt} &amp; = &amp; -r_{01} \left[\mathrm{Ki67-}\right] + 2 r_{10} \left[\mathrm{Cycling}\right] \\
\frac{d\left[\mathrm{Cycling}\right]}{dt} &amp; = &amp;  r_{01} \left[\mathrm{Quiescent}\right] -r_{10} \left[\mathrm{Cycling}\right] \end{aligned}$$</span> Further details on the <em>biology</em> of this model (including details the placement of daughter cells and changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Standard_Models:Death">Death Cycle Models</h2>
<p>PhysiCell currently includes two pre-built death cycle models. More models may be added in future releases, such as autophagy.</p>
<h3 id="sec:Standard_Models:Apoptosis">Apoptosis (<code>apoptosis</code>)<br />
(code: <code>PhysiCell_constants::apoptosis_death_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>Apoptotic</code> with code <code>PhysiCell_constants::apoptotic</code>.</p></li>
</ol>
<p>In this model, apoptotic cells shrink and exit the phase at rate <span class="math inline"><em>r</em><sub>01</sub></span> (with fixed duration <span class="math inline">1/<em>r</em><sub>01</sub></span>). Cells are removed from the simulation at the end of the apoptotic phase. (PhysiCell currently uses a dummy “debris” phase to avoid coding a phase transition from the apoptotic phase to the apoptotic phase; this may be removed in future releases.) See Fig. <a href="#fig:death_model:apoptosis" data-reference-type="ref" data-reference="fig:death_model:apoptosis">[fig:death_model:apoptosis]</a>. The population-scale model is given by: <span class="math display">$$\frac{d\left[\mathrm{Apoptotic}\right]}{dt} = -r_{01} \left[\mathrm{Apoptotic}\right].$$</span> Further details on the <em>biology</em> of this model (including details on changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Standard_Models:Necrosis">Necrosis (<code>necrosis</code>)<br />
(code: <code>PhysiCell_constants::necrosis_death_model</code>)</h3>
<p>This <code>Cycle_Mode</code> has the following <code>Phase</code>s:</p>
<ol>
<li><p><strong>Phase 0:</strong> Named <code>Necrotic (swelling)</code> with code <code>PhysiCell_constants::necrotic_swelling</code>.</p></li>
<li><p><strong>Phase 1:</strong> Named <code>Necrotic (lysed)</code> with code <code>PhysiCell_constants::necrotic_lysed</code>.</p></li>
</ol>
<p>In this model, unlysed necrotic cells swell and attempt to transition to the lysed necrotic phase. There is a block on the transition until the cell reaches a sufficient total volume. Lysed cells gradually shrink (and calcify, if enable) and exit the phase at rate <span class="math inline"><em>r</em><sub>12</sub></span>. Cells are removed from the simulation at the end of the lysed necrotic phase. (PhysiCell currently uses a dummy “debris” phase to avoid coding a phase transition from the lysed necrotic phase phase to another necrotic phase; this may be removed in future releases.) See Fig. <a href="#fig:death_model:necrosis" data-reference-type="ref" data-reference="fig:death_model:necrosis">[fig:death_model:necrosis]</a>.</p>
<p>Further details on the <em>biology</em> of this model (including details on changes in cell volume) and reference parameter values can be found in <span class="citation" data-cites="ref:PhysiCell"></span>.</p>
<div class="mdframed">

</div>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Standard_Models:Volume">Volume model (<code>standard_volume_update_function</code>)</h2>
<p>The standard volume model separately evolves the total fluid volume, cytoplasmic solid volume, and nuclear solid volume, as a system of ODEs (given in <span class="citation" data-cites="ref:PhysiCell"></span>). The standard model also updates cell calcification (but the default rate parameter is zero). See Section <a href="#sec:Volume" data-reference-type="ref" data-reference="sec:Volume">11.3</a> for more information on the <code>Volume</code> class in the <code>Phenotype</code>, and <span class="citation" data-cites="ref:PhysiCell"></span> for the biological details of this model.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Standard_Models:Velocity">Cell velocity model (<code>standard_update_cell_velocity</code>)</h2>
<p>In this model, the cell uses the mechanics interaction data structure to find nearby cells, adds the contributions from adhesion and “repulsion,”, adds the effects of basement membrane interactions (by calling <code>functions.add_cell_basement_membrane_interactions</code>), then computes the contribution to cell velocity by the motility model (by calling <code>update_motility_vector</code>, which in turn calls<br />
<code>functions.update_migration_bias</code>). See Section <a href="#sec:Motility" data-reference-type="ref" data-reference="sec:Motility">11.6</a> for details on motility, Section <a href="#sec:Mechanics" data-reference-type="ref" data-reference="sec:Mechanics">11.5</a> for key cell mechanics phenotype parameters, and Section <a href="#sec:Cells" data-reference-type="ref" data-reference="sec:Cells">9</a> for more information on Cells and their member functions.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:Standard_Models:Orientation">Up orientation model (<code>up_orientation</code>)</h2>
<p>By default 3-D cells have no preferred orientation, and 2-D cells have an “up” orientation (set to [0,0,1]) to ensure they stay in the <span class="math inline"><em>z</em> = 0</span> plane. This supplied function is <code>up_orientation</code>.</p>
<h2 id="sec:Standard_Models:Microenvironment_Phenotype">Oxygen-dependent phenotype<br />
(<code>update_cell_and_death_parameters_O2_based</code>)</h2>
<p>Oxygen-dependent cell proliferation and death rates are so commonly needed in cancer models that we include a model function as standard: <code>update_cell_and_death_parameters_O2_based</code>. Here is the overall model for proliferation:</p>
<ol>
<li><p>Sample the microenvironment for the oxygen concentration <span class="math inline"><em>σ</em></span> at the cell center.</p></li>
<li><p>If <span class="math inline">$\sigma \ge {\small \left[\texttt{parameters.o2\_proliferation\_saturation}\right] }$</span>, then the cycle entry rate is set to 100% of the entry rate in the <code>pReference_live_phenotype</code> reference phenotype.</p></li>
<li><p>If <span class="math inline">$\sigma \le {\small \left[\texttt{parameters.o2\_proliferation\_threshold}\right] }$</span>, then the cycle entry rate is set to 0% of the entry rate in the <code>pReference_live_phenotype</code> reference phenotype.</p></li>
<li><p>Otherwise, the reference cycle entry rate is scaled by <span class="math display">$$\frac{ \sigma - 
{\small \left[\texttt{parameters.o2\_proliferation\_threshold}\right] } }
{ {\small \left[\texttt{parameters.o2\_proliferation\_saturation}\right] } - 
{\small \left[\texttt{parameters.o2\_proliferation\_threshold}\right] } }$$</span></p></li>
</ol>
<p>Here is the overall model for the necrosis death rate:</p>
<ol>
<li><p>Sample the microenvironment for the oxygen concentration <span class="math inline"><em>σ</em></span> at the cell center.</p></li>
<li><p>If <span class="math inline">$\sigma \ge {\small \left[\texttt{parameters.o2\_necrosis\_threshold}\right] }$</span>, then the necrotic death rate is zero.</p></li>
<li><p>If <span class="math inline">$\sigma \le {\small \left[\texttt{parameters.o2\_necrosis\_max}\right] }$</span>, then the necrosis death rate is set to 100% of<br />
<code>parameters.max_necrosis_rate</code>.</p></li>
<li><p>Otherwise, the necrotic death rate is scaled by <span class="math display">$$\frac{ {\small \left[\texttt{parameters.o2\_necrosis\_threshold}\right] } - \sigma }
{{\small \left[\texttt{parameters.o2\_necrosis\_threshold}\right] } - {\small \left[\texttt{parameters.o2\_necrosis\_max}\right] } }$$</span></p></li>
</ol>
<p>This function currently works for the following cell cycle models:</p>
<ol>
<li><p>The Ki67 advanced model (<code>PhysiCell_constants::advanced_Ki67_cycle_model</code>). See Section <a href="#sec:Standard_Models:Ki67_Advanced" data-reference-type="ref" data-reference="sec:Standard_Models:Ki67_Advanced">17.1.3</a>.</p></li>
<li><p>The Ki67 basic model (<code>PhysiCell_constants::basic_Ki67_cycle_model</code>). See Section <a href="#sec:Standard_Models:Ki67_Basic" data-reference-type="ref" data-reference="sec:Standard_Models:Ki67_Basic">17.1.2</a>.</p></li>
<li><p>The Live model (<code>PhysiCell_constants::live_cells_cycle_model</code>). See Section <a href="#sec:Standard_Models:Live" data-reference-type="ref" data-reference="sec:Standard_Models:Live">17.1.1</a>.</p></li>
</ol>
<p>See Section <a href="#sec:Cycle" data-reference-type="ref" data-reference="sec:Cycle">11.1</a> for more on the cell cycle portion of the phenotype, Section ref<span>sec:Death</span> for more information on the death phenotype elements, Section <a href="#sec:Standard_Models:Death" data-reference-type="ref" data-reference="sec:Standard_Models:Death">17.2</a> on standard death models, and Section <a href="#sec:Standard_Models:Cycle" data-reference-type="ref" data-reference="sec:Standard_Models:Cycle">17.1</a> on standard cell cycle models. See <span class="citation" data-cites="ref:PhysiCell"></span> for more on the biology of these models.</p>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:random_functions">Functions for Random Events</h1>
<p>PhysiCell provides several functions for working with random variables and events. All this functionality is based upon C++11 standard, cross-platform functions, using the 64-bit Mersenne Twister for generating random longs. The following functions simplify using random numbers:</p>
<ol>
<li><p><strong><code>long SeedRandom( long input )</code></strong> seeds the pseudo-random number generator with the supplied seed.</p></li>
<li><p><strong><code>long SeedRandom( void )</code></strong> seeds the pseudo-random number generator based upon the system time.</p></li>
<li><p><strong><code>double UniformRandom( void )</code></strong> returns a uniformly distributed random number between 0 and 1.</p></li>
<li><p><strong><code>double NormalRandom( double mean, double standard_deviation ) </code></strong> provides a random number from a Gaussian distribution with mean <code>mean</code> and standard deviation <code>standard_deviation</code>.</p></li>
<li><p><strong><code>int choose_event( std::vector&lt;double&gt;&amp; probabilities ) </code></strong> helps choose a random event based upon the supplied probabilities in the vector <code>probabilities</code> (which must sum to 1). For example, suppose we have events <code>{0, 1, 2, 3}</code> with probabilities <code>{0.01, 0.82, 0.14, 0.03}</code>. Then this code will (on average) return 0 with probability 0.01, return 1 with probability 0.82, and so forth.</p>
<pre><code>std::vector&lt;double&gt; probabilities = {0.01, 0.82, 0.14, 0.03}; 

int number_of_samples = 100000; 
std::vector&lt;int&gt; events( number_of_samples , 0 ); 

//this is thread-safe 
#pragma omp parallel for 
for( int i=0 ; i &lt; number_of_samples ; i++ )
{ events[i] = choose_event( probabilities ); }

std::vector&lt;int&gt; counts( probabilities.size() , 0 ); 
//this is not thread-safe 
for( int i=0 ; i &lt; number_of_samples ; i++ )
{ counts[ events[i] ]++; }

// display counts vs. 
 
std::cout &lt;&lt; &quot;Summary: fraction vs correct fraction &quot; &lt;&lt; std::endl; 
for( int i=0; i &lt; counts.size(); i++)
{
   std::cout &lt;&lt; i &lt;&lt; &quot; : &quot; &lt;&lt; (double) counts[i] / (double) number_of_samples 
             &lt;&lt; &quot; vs &quot; &lt;&lt; probs[i] &lt;&lt; std::endl;
} </code></pre></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:Examples">Examples</h1>
<h2 id="working-with-cell-functions">Working with <code>Cell</code> functions</h2>
<h3 id="sec:Examples:volume_model">Example: a custom volume model</h3>
<p>Here, we will define a simpler volume model that only upates the total volume. We use the mathematical model: <span class="math display">$$\frac{d}{dt} 
{\small \left[\texttt{volume.total}\right] } = r \left( V^* - {\small \left[\texttt{volume.total}\right] } \right),$$</span> where <span class="math display">$$\begin{aligned}
V^* &amp; = &amp; \left( \frac{1 + {\small \left[\texttt{target\_cytoplasmic\_to\_nuclear\_ratio}\right] }}
{1 - {\small \left[\texttt{volume.fluid\_fraction}\right] }} \right) \cdot 
{\small \left[\texttt{volume.target\_solid\_nuclear}\right] } \\
r &amp; = &amp; 
\ln\left( 
\frac{1 - 0.95}{0.5}
\right) {\small \left[\texttt{phenotype.cycle.model.transition\_rate(0,0)}\right] } \end{aligned}$$</span> (This uses the built-in phenotype to get the “target” total volume in terms of the built-in targets, and it sets <span class="math inline"><em>r</em></span> so that a divided cell reaches 95% of its target within the mean duration of the cell’s interdivision time.)</p>
<pre><code>void simple_volume_function( Cell* pCell, Phenotype&amp; phenotype, double dt )
{
    double V_target = phenotype.volume.target_solid_nuclear * 
        (1.0 + phenotype.volume.target_cytoplasmic_to_nuclear_ratio) / 
        (1-phenotype.volume.fluid_fraction); 
    double rate = phenotype.cycle.model().transition_rate(0,0) * log(0.1); 
    
    double addme = V_target; 
    addme -= phenotype.volume.total; 
    addme *= rate; 
    addme *= dt; // dt*rate*( V_target - V )
    
    phenotype.volume.total += addme; 
    
    return; 
}</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Examples:migration">Example: a custom migration bias</h3>
<p>In this example, cells migrate along oxygen gradients. The migration speed is fastest in regions of low oxygen, and the migration is least stochastic (most biased) as the oxygenation increases.</p>
<pre><code>void chemotaxis_bias_function( Cell* pCell, Phenotype&amp; phenotype , double dt )
{
    // quickly find O2 
    static int O2_index = microenvironment.find_density_index( &quot;oxygen&quot; ); 
    
    // sample O2 
    double o2 = pCell-&gt;nearest_density_vector()[O2_index]; 
    
    // set direction along O2 gradients 
    phenotype.motility.migration_bias_direction = pCell-&gt;nearest_gradient(O2_index); 
    normalize( &amp;( phenotype.motility.migration_bias_direction ) ); 
    
    // set speed proportional to O2, scaled by normoxic O2 ( 160 mmHg); 
    // with a maximum of 1.2 micron per minute 
    double theta = o2 / 160.0;
    phenotype.motility.migration_speed = 1.2*(1.0-theta);   
    if( phenotype.motility.migration_speed &gt; 1.2 )
    { phenotype.motility.migration_speed = 1.2; } 

    // the greater the oxygen, the more biased the motion 
    phenotype.motility.migration_bias = theta; 
    
    return; 
}</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Examples:custom_rule">Example: a custom cell rule</h3>
<p>In this example, an immune cell tests nearby cells first for contact, and then for expression of an antigen (a custom variable). The immune cell initiates apoptosis in the target cell with probability that scales with the antigen expression.</p>
<pre><code>void immune_cell_rule( Cell* pCell, Phenotype&amp; phenotype, double dt )
{
    static int antigen_index = 
        pCell-&gt;custom_data.find_variable_index( &quot;antigen&quot; ); 
    static int activation_index = 
        pCell-&gt;custom_data.find_variable_index( &quot;activation&quot; ); 
    
    static int apoptosis_model_index = 
        pCell-&gt;phenotype.death.find_death_model_index( &quot;apoptosis&quot; ); 
    
    // exit if immune function is not yet stimulated, or dead  
    if( pCell-&gt;custom_data[activation_index] &lt; 1e-3 
        || pCell-&gt;phenotype.death.dead == true )
    { return; }

    std::vector&lt;Cell*&gt; nearby = pCell-&gt;cells_in_my_container(); 
    
    // test antigen on nearby cells. stop if you find one 
    // Don&#39;t try to kill dead cells. 
    // Don&#39;t kill yourself 
    Cell* pC = NULL; 
    bool stop = false; 
    int i=0; 
    
    while( !stop &amp;&amp; i &lt; nearby.size() )
    {
        pC = nearby[i]; 
        if( pC-&gt;custom_data[antigen_index] &gt; 1e-3 &amp;&amp; 
            pC-&gt;phenotype.death.dead == false &amp;&amp; 
            pC != pCell )
        { stop = true; } 
        i++; 
        if( stop == false )
        { pC = NULL; }
    }
    
    // if we found a cell, attempt to kill it 
    if( pC )
    {
        double probability = 1.0; // dt*pC-&gt;custom_data[antigen_index]; 
        if( UniformRandom() &lt; probability )
        {
            std::cout &lt;&lt; &quot;death!&quot; &lt;&lt; std::endl; 
            system(&quot;pause&quot;); 
            pC-&gt;start_death( apoptosis_model_index ); 
        }
    }
    return; 
}</code></pre>
<p>Here is the code to add the custom variables to a specific cell:</p>
<pre><code>pCell-&gt;custom_data.add_variable( &quot;antigen&quot;, &quot;dimensionless&quot;, 0.0 ); 
pCell-&gt;custom_data.add_variable( &quot;activation&quot;, &quot;dimensionless&quot;, 0.0 ); </code></pre>
<p>Better still, you could make cell definitions for tumor cells and immune cells:</p>
<pre><code>Cell_Definition immune_cell; 

// operations to define this type 

immune_cell.functions.custom_cell_rule = immune_cell_rule;
immune_cell.custom_data.add_variable( &quot;activation&quot;, &quot;dimensionless&quot;, 0.0 );

Cell_Definition MCF7 = cell_defaults; 
MCF7.custom_data.add_variable( &quot;antigen&quot;, &quot;dimensionless&quot;, 0.0 );</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Examples:phenotype_rule">Example: a custom phenotype update function</h3>
<p>Let’s create a custom phenotype update rule that uses the the standard oxygen-based cell birth and death rates, but also increases cell motility and decreases cell-cel adhesion in low oxygen conditions.</p>
<p>Note that these effects gradually turn on and then saturate based on oxygen values in the cell’s <code>parameters</code>, and we use the cell’s <code>pReference_live_phenotype</code>.</p>
<pre><code>void custom_o2_phenotype_rule( Cell* pCell, Phenotype&amp; phenotype, double dt )
{
   // don&#39;t bother if you&#39;re dead
   if( pCell-&gt;phenotype.death.dead == true )
   { return; }
   
   // first, call the standard function
   update_cell_and_death_parameters_O2_based(pCell,phenotype,dt);     
    
   // next, let&#39;s evaluate the oxygen 
   static int o2_index = microenvironment.find_density_index(&quot;oxygen&quot;); 
   
   double o2 = pCell-&gt;nearest_density_vector()[o2_index];
    
   if( o2 &gt; pCell-&gt;parameters.o2_hypoxic_response )
   { return; }
    
   // interpolation variable 
   double theta = ( pCell-&gt;parameters.o2_hypoxic_response  - o2 )/
      (pCell-&gt;parameters.o2_hypoxic_response - pCell-&gt;parameters.o2_hypoxic_saturation); 
   if( theta &gt; 1.0 )
   { theta = 1.0; } 
    
   // increase the speed of motiltiy up to a max of 1.5 micron/min 
   phenotype.motility.is_motile = true; 
   phenotype.motility.migration_speed = 1.5; 
   phenotype.motility.migration_speed *= theta;  

   phenotype.mechanics.cell_cell_adhesion_strength = (1.0-theta);
   phenotype.mechanics.cell_cell_adhesion_strength *= 
      pCell-&gt;parameters.pReference_live_phenotype-&gt;mechanics.cell_cell_adhesion_strength;
   return; 
}</code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="example-a-custom-velocity-update-function">Example: a custom velocity update function</h3>
<p>We’ll add an example soon. For now, use the default, along with the default motility functions (which allow considerable customization!).</p>
<h3 id="example-analytical-basement-membrane-functions">Example: analytical basement membrane functions</h3>
<p>This space held in reserve.</p>
<h3 id="example-a-custom-cell-orientation-function">Example: a custom cell orientation function</h3>
<p>This space held in reserve.</p>
<h2 id="cell-cycle-models">Cell cycle models</h2>
<h3 id="sec:Examples:custom_cell_cycle">Creating a custom cell cycle model</h3>
<p>Let’s create a simple cycle model, with three phases: Red, Green, and Blue. Red cells become Green. Green cells become Blue. Blue cells divide into two Red cells. Here’s how we accomplish this using the <code>Cycle_Model</code> class. Notice that we’re saving the indices of the newly-created phases for easier reference.</p>
<pre><code>Cycle_Model model;

// set up name information 
model.code = PhysiCell_constants::custom_cycle_model;
mode.name = &quot;Red Green Blue&quot;; 

// add the phases 
int red_index = model.add_phase( 0 , &quot;Red&quot; ); 
int green_index = model.add_phase( 1 , &quot;Green&quot; ); 
int blue_index = model.add_phase( 2 , &quot;Blue&quot; ); 

// set the Blue phase to have division at its end 
model.phases[blue_index].division_at_phase_exit = true; 

// set up the phase links 
model.add_phase_link( red_index , green_index , NULL ); // red -&gt; green
model.add_phase_link( green_index , blue_index , NULL ); // green -&gt; blue
model.add_phase_link( blue_index , red_index , NULL ); // blue -&gt; red 

// set the transition rates
model.transition_rate(red_index,green_index) = 1.0/( 60.0 * 5.0 ); 
     // mean duration: 5 hours
model.transition_rate(green_index,blue_index) = 1.0/( 60.0 * 8.0 ); 
     // mean duration: 8 hours
model.transition_rate(blue_index,red_index) = 1.0/( 60.0 * 2.0 ); 
     // mean duration: 2 hours

// display the model 
model.display( std::cout ); </code></pre>
<p>And this is how we would register that model in a cell definition:</p>
<pre><code>immune_cell.phenotype.cycle.sync_to_cycle_model( rgb_model ); </code></pre>
<p>Or in a single cell:</p>
<pre><code>pCell-&gt;phenotype.cycle.sync_to_cycle_model( rgb_model ); </code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Examples:arrest">Adding an arrest function</h3>
<p>Suppose now that we only want to allow Blue cells to proceed to Red and divide if they have a fluid fraction over 50%. (See Section <a href="#sec:Volume" data-reference-type="ref" data-reference="sec:Volume">11.3</a>.) Then we can define an arrest function:</p>
<pre><code>bool fluid_arrest_function(  Cell* pCell, Phenotype&amp; phenotype, double dt )
{
     if( phenotype.volume.fluid_fraction &lt; 0.5 )
     { return true; }
     return false; 
}</code></pre>
<p>We then assign this arrest function to the transition from the Blue phase to the Red phase:</p>
<pre><code>rgb_model.phase_link(blue_index,red_index).arrest_function = fluid_arrest_function; </code></pre>
<div class="center">
<hr />
<hr />
</div>
<h3 id="sec:Examples:phase_entry">Adding a custom phase entry function</h3>
<p>Suppose now that we want the cell to “mutate” its transition rates whenever it re-enters the Red phase. We can do this with an entry function:</p>
<pre><code>void my_mutation_function( Cell* pCell, Phenotype&amp; phenotype, double dt )
{
     // mutate all transition rates by a uniformly-distributed 
     // number within 10\% of the current value
     double multiplier = 0.9 + 0.2*uniform_random(); 
     phenotype.cycle.data.transition_rate(0,1) *= multiplier; 

     multiplier = 0.9 + 0.2*uniform_random(); 
     phenotype.cycle.data.transition_rate(1,2) *= multiplier; 

     multiplier = 0.9 + 0.2*uniform_random(); 
     phenotype.cycle.data.transition_rate(2,0) *= multiplier; 

     return; 
}</code></pre>
<p>Then, we assign this as the entry function for the Red phase:</p>
<pre><code>rgb_model.phases[red_index].entry_function = my_mutation_function; </code></pre>
<p>Alternatively, we can assign this as the exit function for the Blue-Red transition:</p>
<pre><code>rgb_model.phase_link(blue_index,red_index).exit_function = my_mutation_function; </code></pre>
<div class="center">
<hr />
<hr />
</div>
<h1 id="sec:Future_Plans">Future</h1>
<p>Several features are planned for upcoming PhysiCell releases:</p>
<ol>
<li><p>We will further refine the MultiCellDS output functions to capture more of the cell’s state, including custom variable values. <span style="color: red">(Completed in Version 1.2.2)</span></p></li>
<li><p>We will add functions to read in a saved simulation state.</p></li>
<li><p>We will add an XML-based configuration file. <span style="color: red">(Completed in Version 1.3.0)</span></p></li>
<li><p>We will add a function like <code>void contact_interaction_function(Cell*,Phenotype&amp;,double)</code> to allow cell contact-based signaling and behavior changes.</p></li>
<li><p>We plan to start actively tracking the cell’s list of mechanically interacting neighbors in<br />
<code>cell.state.neighbors</code></p></li>
<li><p>We will further develop <code>cell.state.simple_pressure</code> and provide better examples.</p></li>
<li><p>We will create a standard <code>standard_update_orientation</code> function to let cells rotate towards a preferred orientation (which will be based upon its neighbors).</p></li>
<li><p>We will generalize the cell-cell adhesion model to allow differing levels of adhesion between different types of cells. <span style="color: red">(Completed in Version 1.2.0)</span></p></li>
<li><p>We will merge the <code>Vector_Variable</code> and <code>Variable</code> types for a more unified <code>Custom_Cell_Data</code> struture.</p></li>
<li><p>We may update <code>motilty</code> and associated update functions to build in some hysteresis (bias towards the last direction of the day).</p></li>
<li><p>We will consider partial SBML support for importing molecular-scale models.</p></li>
<li><p>We will continue to refine XML parsing for options and configuration.</p></li>
<li><p>We will allow ellipsoidal cell potential functions for better approximation of cell shapes.</p></li>
<li><p>We will introduce a standard library of simplified (bulk) vasculatures.</p></li>
<li><p>We will introduce a standard library of simplified ECM functions.</p></li>
</ol>
<div class="center">
<hr />
<hr />
</div>
<h1 id="some-notes-on-parameter-values">Some notes on parameter values</h1>
<p>We chose reference proliferation and apoptosis rates for the generic breast epithelium line (calibrated to MCF-10A) so that the apoptotic fraction is approximately 2% <span class="citation" data-cites="ref:MCF10A_apoptosis"></span>, and the net proliferation rate (for the total cell population) is on the order of 0.04 hr<span class="math inline"><sup>-1</sup></span> <span class="citation" data-cites="ref:MultiCellDS ref:MCF10A-NeoST ref:MCF10A_PSON"></span>.</p>
<h2 id="sec:parameters:live">Live cycle model</h2>
<p>For the Live cell model (Section <a href="#sec:Standard_Models:Live" data-reference-type="ref" data-reference="sec:Standard_Models:Live">17.1.1</a>), we fit the system of ODEs <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Live}\right] } &amp; = &amp; (b-d){\small \left[\texttt{Live}\right] } \\
\frac{d}{dt}{\small \left[\texttt{Apoptotic}\right] } &amp; = &amp; d{\small \left[\texttt{Live}\right] } - \frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] }, \end{aligned}$$</span> and we note that <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Total}\right] } 
&amp; = &amp; b {\small \left[\texttt{Live}\right] } - \frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] } \nonumber \\ 
&amp; = &amp; \left( b (1-\textrm{AI}) - \frac{\textrm{AI}}{T_A} \right) {\small \left[\texttt{Total}\right] } \nonumber \\ 
&amp; = &amp; r {\small \left[\texttt{Total}\right] } \end{aligned}$$</span> Here, <span class="math inline"><em>r</em> = 0.04 hr<sup> − 1</sup></span>, <span class="math inline">AI = 0.02</span> is the apoptotic index, and <span class="math inline"><em>T</em><sub><em>A</em></sub> = 8.6 hour</span> (Section <a href="#sec:Standard_Models:Apoptosis" data-reference-type="ref" data-reference="sec:Standard_Models:Apoptosis">17.2.1</a>). Thus, <span class="math display">$$b = \frac{r + \frac{1}{T_A}\textrm{AI}}{1 - \textrm{AI}} \sim 0.0432 \textrm{ hr}^{-1}.$$</span> To get the death rate <span class="math inline"><em>d</em></span>, we use a simple iterative fitting method (see<br />
<code>./documentation/matlab/tune_death_in_live_model</code>) to get <span class="math inline"><em>d</em> ∼ 0.00319 hr<sup> − 1</sup></span>.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:parameters:Ki67_basic">Ki67 Basic model</h2>
<p>For the Ki67 Basic model (Section <a href="#sec:Standard_Models:Ki67_Basic" data-reference-type="ref" data-reference="sec:Standard_Models:Ki67_Basic">17.1.2</a>), we fit the system of ODEs <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Ki67-}\right] } &amp; = &amp; -\left( \frac{1}{T_Q} + d \right) {\small \left[\texttt{Ki67-}\right] } + \frac{2}{T_K}{\small \left[\texttt{Ki67+}\right] }  \\
\frac{d}{dt}{\small \left[\texttt{Ki67+}\right] } &amp; = &amp; \frac{1}{T_Q} {\small \left[\texttt{Ki67-}\right] } - \left( \frac{1}{T_K} + d \right) {\small \left[\texttt{Ki67+}\right] } \\
\frac{d}{dt}{\small \left[\texttt{Apoptotic}\right] } &amp; = &amp; d\left( {\small \left[\texttt{Ki67-}\right] } + {\small \left[\texttt{Ki67+}\right] } \right) -\frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] }, \end{aligned}$$</span> and we note that <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Total}\right] } 
&amp; = &amp; \frac{1}{t_K} {\small \left[\texttt{Ki67+}\right] } - \frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] } \nonumber \\ 
&amp; = &amp; \left( \frac{\textrm{KI}}{T_K} - \frac{\textrm{AI}}{T_A} \right) {\small \left[\texttt{Total}\right] } \nonumber \\ 
&amp; = &amp; r {\small \left[\texttt{Total}\right] } \end{aligned}$$</span> We set <span class="math inline"><em>T</em><sub><em>K</em></sub> = 13 + 2.5</span> hr (the duration of the two phases in the Ki67 Advanced model), <span class="math inline"><em>r</em> = 0.04 hr<sup> − 1</sup></span>, and we set AI = 0.02 as before and keep <span class="math inline"><em>d</em> = 0.00319 hr<sup> − 1</sup></span> from the prior estimate. We thus need to fit <span class="math inline"><em>T</em><sub><em>Q</em></sub></span>. We use a simple iterative fitting method (see <code>./documentation/matlab/tune_Ki67_basic</code>) to get <span class="math inline"><em>T</em><sub><em>Q</em></sub> ∼ 4.59 hr</span>.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:parameters:Ki67_advanced">Ki67 Advanced model</h2>
<p>For the Ki67 Advanced model (Section <a href="#sec:Standard_Models:Ki67_Advanced" data-reference-type="ref" data-reference="sec:Standard_Models:Ki67_Advanced">17.1.3</a>), we fit the system of ODEs <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Ki67-}\right] } &amp; = &amp; -\left( \frac{1}{T_Q} + d \right) {\small \left[\texttt{Ki67-}\right] } + \frac{1}{T_{K2}}{\small \left[\texttt{Ki67+}\right] }_2  \\
\frac{d}{dt}{\small \left[\texttt{Ki67+}\right] }_1 &amp; = &amp; \frac{1}{T_Q} {\small \left[\texttt{Ki67-}\right] } - \left( \frac{1}{T_{K1}} + d \right) {\small \left[\texttt{Ki67+}\right] }_1 \\
\frac{d}{dt}{\small \left[\texttt{Ki67+}\right] }_2 &amp; = &amp;  \frac{2}{T_{K1}} {\small \left[\texttt{Ki67+}\right] }_1 - \left( \frac{1}{T_{K2}} + d \right) {\small \left[\texttt{Ki67+}\right] }_2 \\
\frac{d}{dt}{\small \left[\texttt{Apoptotic}\right] } &amp; = &amp; d\left( {\small \left[\texttt{Ki67-}\right] } + {\small \left[\texttt{Ki67+}\right] }_1 + {\small \left[\texttt{Ki67+}\right] }_2 \right) -\frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] }, \end{aligned}$$</span> and we note that <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Total}\right] } 
&amp; = &amp; \frac{1}{T_{K1}} {\small \left[\texttt{Ki67+}\right] }_1 - \frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] } \nonumber \\ 
&amp; = &amp; \left( \frac{\textrm{KI}_1}{T_{K1}} - \frac{\textrm{AI}}{T_A} \right) {\small \left[\texttt{Total}\right] } \nonumber \\ 
&amp; = &amp; r {\small \left[\texttt{Total}\right] } \end{aligned}$$</span> We set <span class="math inline"><em>T</em><sub><em>K</em>1</sub> = 13</span> hr, <span class="math inline"><em>T</em><sub><em>K</em>2</sub> = 2.5</span> hr, <span class="math inline"><em>T</em><sub><em>A</em></sub> = 8.6</span> hr, and <span class="math inline"><em>r</em> = 0.04 hr<sup> − 1</sup></span>, and we set AI = 0.02 as before and keep <span class="math inline"><em>d</em> = 0.00319 hr<sup> − 1</sup></span> from the prior estimate. We thus need to fit <span class="math inline"><em>T</em><sub><em>Q</em></sub></span>. We use a simple iterative fitting method (see <code>./documentation/matlab/tune_Ki67_advanced</code>) to get <span class="math inline"><em>T</em><sub><em>Q</em></sub> ∼ 3.62 hr</span> for this model. <span class="citation" data-cites="ref:Ki67_MCF10A"></span>.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:parameters:flow_cytometry">Flow Cytometry model</h2>
<p>For the Flow Cytometry model (Section <a href="#sec:Standard_Models:Flow_Cytometry" data-reference-type="ref" data-reference="sec:Standard_Models:Flow_Cytometry">17.1.4</a>), we fit the system of ODEs <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{G0G1}\right] } &amp; = &amp; -\left( \frac{1}{T_{G0G1}} + d \right) {\small \left[\texttt{G0G1}\right] } + \frac{2}{T_{G2M}}{\small \left[\texttt{G2M}\right] }  \\
\frac{d}{dt}{\small \left[\texttt{S}\right] } &amp; = &amp; \frac{1}{T_{G0G1}} {\small \left[\texttt{G0G1}\right] } - \left( \frac{1}{T_{S}} + d \right) {\small \left[\texttt{S}\right] } \\
\frac{d}{dt}{\small \left[\texttt{G2M}\right] } &amp; = &amp;  \frac{1}{T_{S}} {\small \left[\texttt{S}\right] } - \left( \frac{1}{T_{G2M}} + d \right) {\small \left[\texttt{G2M}\right] } \\
\frac{d}{dt}{\small \left[\texttt{Apoptotic}\right] } &amp; = &amp; d\left( {\small \left[\texttt{G0G1}\right] } + {\small \left[\texttt{S}\right] } + {\small \left[\texttt{G2M}\right] } \right) -\frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] }, \end{aligned}$$</span> and we note that <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Total}\right] } 
&amp; = &amp; \frac{1}{T_{G2M}} {\small \left[\texttt{G2M}\right] } - \frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] } \nonumber \\ 
&amp; = &amp; \left( \frac{1}{T_{G2M}} \frac{{\small \left[\texttt{G2M}\right] }}{{\small \left[\texttt{Total}\right] }} - \frac{\textrm{AI}}{T_A} \right) {\small \left[\texttt{Total}\right] } \nonumber \\ 
&amp; = &amp; r {\small \left[\texttt{Total}\right] } \end{aligned}$$</span> For consistency with our estimates for the Ki67-Advanced model (see Section <a href="#sec:parameters:Ki67_advanced" data-reference-type="ref" data-reference="sec:parameters:Ki67_advanced">21.3</a>), we set <span class="math inline"><em>T</em><sub><em>S</em></sub> = 8</span> hr, <span class="math inline"><em>T</em><sub><em>G</em>2<em>M</em></sub> = <em>T</em><sub><em>G</em>2</sub> + <em>T</em><sub><em>M</em></sub> = 5</span> hr, <span class="math inline"><em>T</em><sub><em>A</em></sub> = 8.6</span> hr, and <span class="math inline"><em>r</em> = 0.04 hr<sup> − 1</sup></span>, and we set AI = 0.02 as before and keep <span class="math inline"><em>d</em> = 0.00319 hr<sup> − 1</sup></span> from the prior estimates. We thus need to fit <span class="math inline"><em>T</em><sub><em>G</em>0<em>G</em>1</sub></span>. We use a simple iterative fitting method (see <code>./documentation/matlab/tune_cytometry</code>) to get <span class="math inline"><em>T</em><sub><em>G</em>0<em>G</em>1</sub> ∼ 5.15 hr</span> for this model. <span class="citation" data-cites="ref:Ki67_MCF10A"></span>.</p>
<div class="center">
<hr />
<hr />
</div>
<h2 id="sec:parameters:flow_cytometry_separated">Separated Flow Cytometry model</h2>
<p>For the Flow Cytometry model (Section <a href="#sec:Standard_Models:Flow_Cytometry_Separated" data-reference-type="ref" data-reference="sec:Standard_Models:Flow_Cytometry_Separated">17.1.5</a>), we fit the system of ODEs <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{G0G1}\right] } &amp; = &amp; -\left( \frac{1}{T_{G0G1}} + d \right) {\small \left[\texttt{G0G1}\right] } + \frac{2}{T_{M}}{\small \left[\texttt{M}\right] }  \\
\frac{d}{dt}{\small \left[\texttt{S}\right] } &amp; = &amp; \frac{1}{T_{G0G1}} {\small \left[\texttt{G0G1}\right] } - \left( \frac{1}{T_{S}} + d \right) {\small \left[\texttt{S}\right] } \\
\frac{d}{dt}{\small \left[\texttt{G2}\right] } &amp; = &amp;  \frac{1}{T_{S}} {\small \left[\texttt{S}\right] } - \left( \frac{1}{T_{G2}} + d \right) {\small \left[\texttt{G2}\right] } \\
\frac{d}{dt}{\small \left[\texttt{M}\right] } &amp; = &amp;  \frac{1}{T_{G2}} {\small \left[\texttt{G2}\right] } - \left( \frac{1}{T_{M}} + d \right) {\small \left[\texttt{M}\right] } \\
\frac{d}{dt}{\small \left[\texttt{Apoptotic}\right] } &amp; = &amp; d\left( {\small \left[\texttt{G0G1}\right] } + {\small \left[\texttt{S}\right] } + {\small \left[\texttt{G2}\right] } + {\small \left[\texttt{M}\right] } \right) -\frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] }, \end{aligned}$$</span> and we note that <span class="math display">$$\begin{aligned}
\frac{d}{dt}{\small \left[\texttt{Total}\right] } 
&amp; = &amp; \frac{1}{T_{M}} {\small \left[\texttt{M}\right] } - \frac{1}{T_A} {\small \left[\texttt{Apoptotic}\right] } \nonumber \\ 
&amp; = &amp; \left( \frac{{\small \left[\texttt{MI}\right] }}{T_{M}}  - \frac{\textrm{AI}}{T_A} \right) {\small \left[\texttt{Total}\right] } \nonumber \\ 
&amp; = &amp; r {\small \left[\texttt{Total}\right] },\end{aligned}$$</span> where <span class="math inline">${\small \left[\texttt{MI}\right] }$</span> is the mitotic index.</p>
<p>For consistency with our estimates for the Ki67-Advanced model (see Section <a href="#sec:parameters:Ki67_advanced" data-reference-type="ref" data-reference="sec:parameters:Ki67_advanced">21.3</a>), we set <span class="math inline"><em>T</em><sub><em>S</em></sub> = 8</span> hr, <span class="math inline"><em>T</em><sub><em>G</em>2</sub> = 4</span> h, <span class="math inline"><em>T</em><sub><em>M</em></sub> = 1</span> hr, <span class="math inline"><em>T</em><sub><em>A</em></sub> = 8.6</span> hr, and <span class="math inline"><em>r</em> = 0.04 hr<sup> − 1</sup></span>, and we set AI = 0.02 as before and keep <span class="math inline"><em>d</em> = 0.00319 hr<sup> − 1</sup></span> from the prior estimates. We thus need to fit <span class="math inline"><em>T</em><sub><em>G</em>0<em>G</em>1</sub></span>. We use a simple iterative fitting method (see <code>./documentation/matlab/tune_cytometry_separated</code>) to get <span class="math inline"><em>T</em><sub><em>G</em>0<em>G</em>1</sub> ∼ 4.98 hr</span> for this model. <span class="citation" data-cites="ref:Ki67_MCF10A"></span>.</p>
<div class="center">
<hr />
<hr />
</div>
<h1 id="acknowledgements">Acknowledgements</h1>
<p>We thank the Breast Cancer Research Foundation, the Jayne Koskinas Ted Giovanis Foundation for Health and Policy, and the National Cancer Institute for past and present funding for PhysiCell. We gratefully acknowledge the encouragement and suport of the multiscale modeling community as we developed and refined MultiCellDS. We hope the community finds this software useful!</p>
<p>Paul Macklin thanks the Chaste, CompuCell3D, COPASI, and Morpheus communities and developers for Open Source leadership and inspiration.</p>
<div class="center">
<hr />
<hr />
</div>
