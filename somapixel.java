import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import java.awt.HeadlessException;
import java.awt.Image;
import java.awt.RenderingHints;
import java.awt.Transparency;
import java.awt.image.BufferedImage;
import java.awt.image.ImageProducer;
import java.awt.image.ImageObserver;
import java.awt.image.PixelGrabber;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.io.File;
import javax.imageio.ImageIO;

public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Image img01 = null;
        Image img02 = null;

        BufferedImage bfi = null;
//        BufferedImage bfi1 = null;
//        BufferedImage bfi2 = null;
        BufferedImage bfi3 = null;

        try {
            img01 = ImageIO.read(new File("img01.bmp"));
            img02 = ImageIO.read(new File("img02.bmp"));
        } catch (Exception e) {
            // TODO: handle exception
        }

        int pixel1;
        int pixel2;
        int widthImg01 = img01.getWidth(null);
        int widthImg02 = img02.getWidth(null);
        int heightImg01 = img01.getHeight(null);
        int heightImg02 = img02.getHeight(null);


        int totalwidth = widthImg01 * 3;// widthImg02;
        int totalHeigh = heightImg01;

        //Acusa erro caso as imagens sejam de tamanhos diferentes
        if ((widthImg01 != widthImg02) || (heightImg01 != heightImg02)) {
            System.out.println("Imagens de tamanho diferentes!");
        }

        bfi = new BufferedImage(totalwidth, totalHeigh, BufferedImage.TYPE_INT_ARGB);
//        BufferedImage bfi1 = createBufferedImage(img01);
//        BufferedImage bfi2 = createBufferedImage(img02);
        BufferedImage bfi1 = toBufferedImage(img01);
        BufferedImage bfi2 = toBufferedImage(img02);

        bfi3 = new BufferedImage(widthImg01, heightImg01, BufferedImage.TYPE_INT_ARGB);

        // handlepixels(img01, 0, 0, widthImg01, heightImg01);


        for (int j = 0; j < heightImg01; j++) {
            for (int i = 0; i < widthImg01; i++) {

                pixel1 = bfi1.getRGB(i, j);
                pixel2 = bfi2.getRGB(i, j);
                Color color1 = new Color(pixel1);
                Color color2 = new Color(pixel2);

                int red   = (color1.getRed()   + color2.getRed())   % 256;
                int green = (color1.getGreen() + color2.getGreen()) % 256;
                int blue  = (color1.getBlue()  + color2.getBlue())  % 256;
                
                Color color3 = new Color(red, green, blue);
                bfi3.setRGB(i, j, color3.getRGB());
            }
        }

        //Ajustes de Imagem
        Graphics g = bfi.getGraphics();


        ((Graphics2D) g).setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        ((Graphics2D) g).setRenderingHint(RenderingHints.KEY_FRACTIONALMETRICS, RenderingHints.VALUE_FRACTIONALMETRICS_ON);
        ((Graphics2D) g).setRenderingHint(RenderingHints.KEY_ALPHA_INTERPOLATION, RenderingHints.VALUE_ALPHA_INTERPOLATION_QUALITY);
        ((Graphics2D) g).setRenderingHint(RenderingHints.KEY_COLOR_RENDERING, RenderingHints.VALUE_COLOR_RENDER_QUALITY);
        ((Graphics2D) g).setRenderingHint(RenderingHints.KEY_RENDERING, RenderingHints.VALUE_RENDER_QUALITY);
        ((Graphics2D) g).setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);

// Preenche o plano de fundo da pagina com branco
        g.setColor(Color.GREEN);
        g.fillRect(0, 0, totalwidth, totalHeigh);
        //g.fillRect(0, 0, widthImg01, heightImg01);

        g.drawImage(img01, 0, 0, null);
        g.drawImage(img02, widthImg01, 0, null);
        g.drawImage(bfi3, widthImg01 + widthImg02, 0, null);
        // g.drawImage(bfi, widthImg01 + widthImg02, 0, null);


        //Fru Fru... adiciona uma linha prtea para separar as imagens
        g.setColor(Color.BLACK);
        g.fillRect(widthImg01, 0, 5, totalHeigh);

//Exibe o resultado final
        JFrame fr = new JFrame("Merge de imagens");
        fr.getContentPane().setLayout(new BorderLayout());
        JLabel jl = new JLabel(new ImageIcon(bfi));
        fr.getContentPane().add(jl, BorderLayout.CENTER);
        fr.pack();
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setVisible(true);
    }

//    private static BufferedImage createBufferedImage(Image image) {
//        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
//        BufferedImage bm = null;
//        try {
//            // Determine the type of transparency of the new buffered image
//            int transparency = Transparency.OPAQUE;
////            if (hasAlpha) { transparency = Transparency.BITMASK; }
//            // Create the buffered image
//            GraphicsDevice gs = ge.getDefaultScreenDevice();
//            GraphicsConfiguration gc = gs.getDefaultConfiguration();
//            bm = gc.createCompatibleImage(image.getWidth(null), image.getHeight(null), transparency);
//        } catch (HeadlessException e) {
//            // The system does not have a screen
//        }
//        return bm;
//    }
// This method returns a buffered image with the contents of an image 

    public static BufferedImage toBufferedImage(Image image) {
        if (image instanceof BufferedImage) {
            return (BufferedImage) image;
        }
        // This code ensures that all the pixels in the image are loaded
        image = new ImageIcon(image).getImage();
        // Determine if the image has transparent pixels; for this method's
        // implementation, see Determining If an Image Has Transparent Pixels
        boolean hasAlpha = hasAlpha(image);
        // Create a buffered image with a format that's compatible with the screen
        BufferedImage bimage = null;
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        try {
            // Determine the type of transparency of the new buffered image
            int transparency = Transparency.OPAQUE;
            if (hasAlpha) {
                transparency = Transparency.BITMASK;
            }
            // Create the buffered image
            GraphicsDevice gs = ge.getDefaultScreenDevice();
            GraphicsConfiguration gc = gs.getDefaultConfiguration();
            bimage = gc.createCompatibleImage(image.getWidth(null), image.getHeight(null), transparency);
        } catch (HeadlessException e) {
            // The system does not have a screen
        }
        if (bimage == null) {
            // Create a buffered image using the default color model
            int type = BufferedImage.TYPE_INT_RGB;
            if (hasAlpha) {
                type = BufferedImage.TYPE_INT_ARGB;
            }
            bimage = new BufferedImage(image.getWidth(null), image.getHeight(null), type);
        }
        // Copy image to buffered image
        Graphics g = bimage.createGraphics();
        // Paint the image onto the buffered image
        g.drawImage(image, 0, 0, null);
        g.dispose();
        return bimage;
    }

    public static boolean hasAlpha(Image image) {

        // If buffered image, the color model is readily available
        if (image instanceof BufferedImage) {
            return ((BufferedImage) image).getColorModel().hasAlpha();
        }

        // Use a pixel grabber to retrieve the image's color model;
        // grabbing a single pixel is usually sufficient
        PixelGrabber pg = new PixelGrabber(image, 0, 0, 1, 1, false);

        try {
            pg.grabPixels();
        } catch (InterruptedException e) {
        }
        // Get the image's color model
        return pg.getColorModel().hasAlpha();
    }
}