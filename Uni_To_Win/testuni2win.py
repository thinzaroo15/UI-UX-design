import unittest
import Uni_To_Win

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        win = u'''vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? arG;zGm;vmolrsm; jzpfonf/
        xdkolwdkYü ydkif;jcm; a0zefwwfaom ÓPfESihf usihf0wf odwwfaom pdwfwdkY½SdMuí xdkolwdkYonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        unicode = u'''လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။
        ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article One")

    def test_article_two(self):
        win = u'''vlwdkif;onf vlYtcGihf ta&; aMunmpmwrf;wGif azmfjyxm;onhf tcGihfta&; tm;vkH;? vGwfvyfcGihf tm;vkH;wdkYudk ydkifqdkif cHpm;cGihf½Sdonf/
        vlrsdK;EG,ftm;jzihf jzpfap? tom;ta&miftm;jzihf jzpfap? usm;? r? obm0tm;jzihf jzpfap? bmompum;tm;jzihf jzpfap? udk;uG,fonhf bmomtm;jzihf jzpfap? EdkifiHa&;,lqcsuf?
        odkYwnf;r[kwf tjcm;,lqcsuftm;jzihf jzpfap? EdkifiHESihf qdkifaom? odkYwnf;r[kwf vlrItqihftwef;ESihf qdkifaom Zpfjrpf tm;jzihfjzpfap?
        ypönf; Opöm *kPftm;jzihf jzpfap? rsdK;½dk;Zmwdtm;jzihf jzpfap? tjcm; tqihftwef; tm;jzihf jzpfap cGJjcm;jcif;r½Sdap&/
        xdkYjyif vlwpfOD; wpfa,muf aexdkif&m EdkifiH\ odkYwnf;r[kwf e,fajra'o\ EdkifiHa&;qdkif&m jzpfap pD&ifydkifcGihfqdkif&m jzpfap wdkif;jynf tcsif;csif; qdkif&mjzpfap?
        tqihftwef; wpfckckudk tajcûyí aomfvnf;aumif;? a'oe,fajrwpfckonf tcsKyftjcm tmPmydkif vGwfvyfonhf e,fajr? odkYwnf;r[kwf ukvor*¾ xdef;odrf; apmihfa½Smuf xm;&onhf e,fajr?
        odkYwnf;r[kwf udk,fydkif tkyfcsKyfcGihf tmPmwdkY wpdwfwa'oavmufom &½Sdonhf e,fajr pojzihf ,if;odkY aom e,fajrrsm; jzpfonf [laom taMumif;udk taxmuftxm; ûyí aomfvnf;aumif; cGJjcm;jcif; vkH;0 r½Sdap&/'''
        unicode = u'''လူတိုင်းသည် လူ့အခွင့် အရေး ကြေညာစာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေး အားလုံး၊ လွတ်လပ်ခွင့် အားလုံးတို့ကို ပိုင်ဆိုင် ခံစားခွင့်ရှိသည်။
        လူမျိုးနွယ်အားဖြင့် ဖြစ်စေ၊ အသားအရောင်အားဖြင့် ဖြစ်စေ၊ ကျား၊ မ၊ သဘာဝအားဖြင့် ဖြစ်စေ၊ ဘာသာစကားအားဖြင့် ဖြစ်စေ၊ ကိုးကွယ်သည့် ဘာသာအားဖြင့် ဖြစ်စေ၊ နိုင်ငံရေးယူဆချက်၊
        သို့တည်းမဟုတ် အခြားယူဆချက်အားဖြင့် ဖြစ်စေ၊ နိုင်ငံနှင့် ဆိုင်သော၊ သို့တည်းမဟုတ် လူမှုအဆင့်အတန်းနှင့် ဆိုင်သော ဇစ်မြစ် အားဖြင့်ဖြစ်စေ၊
        ပစ္စည်း ဥစ္စာ ဂုဏ်အားဖြင့် ဖြစ်စေ၊ မျိုးရိုးဇာတိအားဖြင့် ဖြစ်စေ၊ အခြား အဆင့်အတန်း အားဖြင့် ဖြစ်စေ ခွဲခြားခြင်းမရှိစေရ။
        ထို့ပြင် လူတစ်ဦး တစ်ယောက် နေထိုင်ရာ နိုင်ငံ၏ သို့တည်းမဟုတ် နယ်မြေဒေသ၏ နိုင်ငံရေးဆိုင်ရာ ဖြစ်စေ စီရင်ပိုင်ခွင့်ဆိုင်ရာ ဖြစ်စေ တိုင်းပြည် အချင်းချင်း ဆိုင်ရာဖြစ်စေ၊
        အဆင့်အတန်း တစ်ခုခုကို အခြေပြု၍ သော်လည်းကောင်း၊ ဒေသနယ်မြေတစ်ခုသည် အချုပ်အခြာ အာဏာပိုင် လွတ်လပ်သည့် နယ်မြေ၊ သို့တည်းမဟုတ် ကုလသမဂ္ဂ ထိန်းသိမ်း စောင့်ရှောက် ထားရသည့် နယ်မြေ၊
        သို့တည်းမဟုတ် ကိုယ်ပိုင် အုပ်ချုပ်ခွင့် အာဏာတို့ တစိတ်တဒေသလောက်သာ ရရှိသည့် နယ်မြေ စသဖြင့် ယင်းသို့ သော နယ်မြေများ ဖြစ်သည် ဟူသော အကြောင်းကို အထောက်အထား ပြု၍ သော်လည်းကောင်း ခွဲခြားခြင်း လုံးဝ မရှိစေရ။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Two")

    def test_article_three(self):
        win = u'''vlwdkif;ü touf½Sif&ef vGwfvyfrIcGihfESihf vkHûcHpdwfcscGihf ½Sdonf/'''
        unicode = u'''လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Three")

    def test_article_four(self):
        win = u'''rnfoludkrQ aus;uReftjzpf? odkYwnf;r[kwf taptyg;tjzpf? EdkifxufpD;eif; apcdkif;jcif; rûy&? vludk aus;uRefozG,f t"r® apcdkif;jcif;? ta&mif;t0,f ûyjcif;ESihf
        xdkoabm oufa&mufaom vkyfief;[lorQudk ydwfyif wm;jrpf &rnf/'''
        unicode = u'''မည်သူကိုမျှ ကျေးကျွန်အဖြစ်၊ သို့တည်းမဟုတ် အစေအပါးအဖြစ်၊ နိုင်ထက်စီးနင်း စေခိုင်းခြင်း မပြုရ၊ လူကို ကျေးကျွန်သဖွယ် အဓမ္မ စေခိုင်းခြင်း၊ အရောင်းအဝယ် ပြုခြင်းနှင့်
        ထိုသဘော သက်ရောက်သော လုပ်ငန်းဟူသမျှကို ပိတ်ပင် တားမြစ် ရမည်။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Four")

    def test_article_five(self):
        win = u'''rnfoludkrQ n§Úf;yef; ESdyfpufjcif;? odkYwnf;r[kwf &ufpufMurf;êuwfpGm vlrqefpGm *kPfi,fapaom qufqHrI rûy&? odkYwnf;r[kwf tjypf'Pf ay;jcif;rûy&/'''
        unicode = u'''မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊ သို့တည်းမဟုတ် ရက်စက်ကြမ်းကြုတ်စွာ လူမဆန်စွာ ဂုဏ်ငယ်စေသော ဆက်ဆံမှု မပြုရ၊ သို့တည်းမဟုတ် အပြစ်ဒဏ် ပေးခြင်းမပြုရ။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Five")

    def test_article_six(self):
        win = u'''vlwdkif;wGif Oya't&mü vlyk*¾dKvfwpfOD; tjzpfjzihf t&mcyfodrf;wGif todtrSwf ûyjcif;udk cH,lydkifcGihf½Sdonf/'''
        unicode = u'''လူတိုင်းတွင် ဥပဒေအရာ၌ လူပုဂ္ဂိုလ်တစ်ဦး အဖြစ်ဖြင့် အရာခပ်သိမ်းတွင် အသိအမှတ် ပြုခြင်းကို ခံယူပိုင်ခွင့်ရှိသည်။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Six")

    def test_article_seven(self):
        win = u'''vltm;vkH;wdkYonf Oya't&mü wlnDMuonhftjyif? Oya'\ tumtuG,fudk jcm;em;jcif; rcH&apbJ wlnDpGm cHpm;ydkifcGihf½Sdonf/
        þaMunm pmwrf;yg oabmw&m;rsm;udk zDqefí cGJjcm;jcif;rS vnf;aumif;? xdkodkYcGJjcm;jcif;udk vIHhaqmfjcif;rS vnf;aumif;? uif;vGwf ap&ef tumtuG,fudk wlnDpGm cHpm;ydkifcGihf ½Sdonf/'''
        unicode = u'''လူအားလုံးတို့သည် ဥပဒေအရာ၌ တူညီကြသည့်အပြင်၊ ဥပဒေ၏ အကာအကွယ်ကို ခြားနားခြင်း မခံရစေဘဲ တူညီစွာ ခံစားပိုင်ခွင့်ရှိသည်။
        ဤကြေညာ စာတမ်းပါ သဘောတရားများကို ဖီဆန်၍ ခွဲခြားခြင်းမှ လည်းကောင်း၊ ထိုသို့ခွဲခြားခြင်းကို လှုံ့ဆော်ခြင်းမှ လည်းကောင်း၊ ကင်းလွတ် စေရန် အကာအကွယ်ကို တူညီစွာ ခံစားပိုင်ခွင့် ရှိသည်။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Seven")

    def test_article_eight(self):
        win = u'''zGJUpnf;ykH tajccHOya'u aomfvnf;aumif; tjcm; Oya'u aomfvnf;aumif; vlwdkif;twGuf ay;xm;onhf tajccH tcGihfta&; rsm;onf csdK;azmuf zsufqD;jcif;cHcJh&vQif
        xdkodkY csdK;azmufzsufqD; aom ûyvkyfrIaMumihf jzpfay:vmaom epfemcsuf twGuf xdkolonf EdkifiHqdkif&m tmPmydkifw&m;½kH;wGif xda&mufpGm oufomcGihf ½SdEdkifap&rnf/'''
        unicode = u'''ဖွဲ့စည်းပုံ အခြေခံဥပဒေက သော်လည်းကောင်း အခြား ဥပဒေက သော်လည်းကောင်း လူတိုင်းအတွက် ပေးထားသည့် အခြေခံ အခွင့်အရေး များသည် ချိုးဖောက် ဖျက်ဆီးခြင်းခံခဲ့ရလျှင်
        ထိုသို့ ချိုးဖောက်ဖျက်ဆီး သော ပြုလုပ်မှုကြောင့် ဖြစ်ပေါ်လာသော နစ်နာချက် အတွက် ထိုသူသည် နိုင်ငံဆိုင်ရာ အာဏာပိုင်တရားရုံးတွင် ထိရောက်စွာ သက်သာခွင့် ရှိနိုင်စေရမည်။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Eight")

    def test_article_nine(self):
        win = u'''rnfolrQ Oya't& r[kwfaom zrf;qD;jcif;udk jzpfap? csKyfaESmifjcif;udk jzpfap? jynfESifjcif;udkjzpfap rcHap&/'''
        unicode = u'''မည်သူမျှ ဥပဒေအရ မဟုတ်သော ဖမ်းဆီးခြင်းကို ဖြစ်စေ၊ ချုပ်နှောင်ခြင်းကို ဖြစ်စေ၊ ပြည်နှင်ခြင်းကိုဖြစ်စေ မခံစေရ။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Nine")

    def test_article_ten(self):
        win = u'''tcGihfta&;rsm;ESihf wm0ef 0wÅ&m;rsm;udk tqkH;tjzwfcH&mwGif vnf;aumif;? jypfrIaMumihf w&m;pGJqdk pD&if qkH;jzwfcH&mwGif vnf;aumif;?
        vlwdkif;onf vGwfvyfí bufrvdkufaom w&m;½kH;awmf\ vltrsm; a½SUarSmufwGif rQwpGm Mum;emppfaq;jcif;udk wlnDpGm cHpm; ydkifcGihf½Sdonf/'''
        unicode = u'''အခွင့်အရေးများနှင့် တာဝန် ဝတ္တရားများကို အဆုံးအဖြတ်ခံရာတွင် လည်းကောင်း၊ ပြစ်မှုကြောင့် တရားစွဲဆို စီရင် ဆုံးဖြတ်ခံရာတွင် လည်းကောင်း၊
        လူတိုင်းသည် လွတ်လပ်၍ ဘက်မလိုက်သော တရားရုံးတော်၏ လူအများ ရှေ့မှောက်တွင် မျှတစွာ ကြားနာစစ်ဆေးခြင်းကို တူညီစွာ ခံစား ပိုင်ခွင့်ရှိသည်။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article ten")

    def test_article_eleven(self):
        win = u'''vltrsm; a½SUarSmufü Oya'twdkif; ppfaq;í jypfrIusL;vGefonf[k xif½Sm; pD&ifjcif;cH&onhf tcsdeftxd jypfrIESihf w&m;pGJqdkjcif; cH&olwdkif;onf tjypfrJhol[lí ,lq jcif;cHxdkufonhf tcGihfta&;½Sdonf/
        xdktrIudk Mum;emppfaq;&m0,f pGyfpGJcH&onhf jypfrItwGuf ckcHacsyEdkif&ef vdktyfaom tcGihfta&;rsm;udk xdkoltm; ay;NyD; jzpfap&rnf/
        vlwpfOD;wpfa,muftm; EdkifiHOya't&jzpfap? tjynfjynfqdkif&m Oya't& jzpfap? jypfrIrajrmufaom vkyf&yf odkYr[kwf ysufuGufrIt& qGJqdkjypfay;jcif; rûy&/
        xdkYtjyif jypfrIusL;vGefpÚftcgu xdkufoihfapEdkifaom tjypf'PfxufydkrdkBuD;av;aom tjypf'Pfudk xdkufoihfjcif;r½Sdap&/'''
        unicode = u'''လူအများ ရှေ့မှောက်၌ ဥပဒေအတိုင်း စစ်ဆေး၍ ပြစ်မှုကျူးလွန်သည်ဟု ထင်ရှား စီရင်ခြင်းခံရသည့် အချိန်အထိ ပြစ်မှုနှင့် တရားစွဲဆိုခြင်း ခံရသူတိုင်းသည် အပြစ်မဲ့သူဟူ၍ ယူဆ ခြင်းခံထိုက်သည့် အခွင့်အရေးရှိသည်။
        ထိုအမှုကို ကြားနာစစ်ဆေးရာဝယ် စွပ်စွဲခံရသည့် ပြစ်မှုအတွက် ခုခံချေပနိုင်ရန် လိုအပ်သော အခွင့်အရေးများကို ထိုသူအား ပေးပြီး ဖြစ်စေရမည်။
        လူတစ်ဦးတစ်ယောက်အား နိုင်ငံဥပဒေအရဖြစ်စေ၊ အပြည်ပြည်ဆိုင်ရာ ဥပဒေအရ ဖြစ်စေ၊ ပြစ်မှုမမြောက်သော လုပ်ရပ် သို့မဟုတ် ပျက်ကွက်မှုအရ ဆွဲဆိုပြစ်ပေးခြင်း မပြုရ။
        ထို့အပြင် ပြစ်မှုကျူးလွန်စဉ်အခါက ထိုက်သင့်စေနိုင်သော အပြစ်ဒဏ်ထက်ပိုမိုကြီးလေးသော အပြစ်ဒဏ်ကို ထိုက်သင့်ခြင်းမရှိစေရ။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article eleven")

    # def test_article_twelve(self):
    #     win = u'''rnfolrQ rdrdoabmtwdkif; at;csrf;vGwfvyfpGm aexdkifjcif;udk aomfvnf;aumif;? rdrd\ rdom;pkudk aomfvnf;aumif;? rdrd\ aetdrf todkuft0ef;udk aomfvnf;aumif;? pmay;pm,ludk aomfvnf;aumif;? Oya't& r[kwfaom 0ifa&muf pGufzufjcif; rcHap&/
    #     xdkYjyif rdrd\*kPfodu©m udkvnf; txufyg twdkif; ykwfcwfjcif; rcHap&/ vlwdkif;wGif xdkodkY 0ifa&mufpGufzufjcif;rS aomfvnf;aumif; ykwfcwfjcif;rS aomfvnf;aumif; Oya't& umuG,f ydkifcGihf½Sdonf/'''
    #     unicode = u'''မည်သူမျှ မိမိသဘောအတိုင်း အေးချမ်းလွတ်လပ်စွာ နေထိုင်ခြင်းကို သော်လည်းကောင်း၊ မိမိ၏ မိသားစုကို သော်လည်းကောင်း၊ မိမိ၏ နေအိမ် အသိုက်အဝန်းကို သော်လည်းကောင်း၊ စာပေးစာယူကို သော်လည်းကောင်း၊ ဥပဒေအရ မဟုတ်သော ဝင်ရောက် စွက်ဖက်ခြင်း မခံစေရ။
    #     ထို့ပြင် မိမိ၏ဂုဏ်သိက္ခာ ကိုလည်း အထက်ပါ အတိုင်း ပုတ်ခတ်ခြင်း မခံစေရ။ လူတိုင်းတွင် ထိုသို့ ဝင်ရောက်စွက်ဖက်ခြင်းမှ သော်လည်းကောင်း ပုတ်ခတ်ခြင်းမှ သော်လည်းကောင်း ဥပဒေအရ ကာကွယ် ပိုင်ခွင့်ရှိသည်။'''
    #     result = Uni_To_Win.convert(unicode)
    #     self.assertEqual(win, result, "Failed converting Test Article Twelve")

    def test_article_thirteen(self):
        win = u'''vlwdkif;wGif rdrd\EdkifiH e,fedrdwf twGif;ü vGwfvyfpGm oGm;vm a½TUajymif; EdkifcGihf? aexdkifcGihf½Sdonf/'''
        unicode = u'''လူတိုင်းတွင် မိမိ၏နိုင်ငံ နယ်နိမိတ် အတွင်း၌ လွတ်လပ်စွာ သွားလာ ရွှေ့ပြောင်း နိုင်ခွင့်၊ နေထိုင်ခွင့်ရှိသည်။'''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Thirteen")

    def test_article_fourteen(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Fourteen")

    def test_article_fifteen(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Fifteen")

    def test_article_sixteen(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Sixteen")

    def test_article_seventeen(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Seventeen")

    def test_article_eighteen(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Eighteen")

    def test_article_nineteen(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Nineteen")

    def test_article_twenty(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Twenty")

    def test_article_twentyOne(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentyOne")

    def test_article_twentyTwo(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentyTwo")

    def test_article_twentyThree(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentyThree")

    def test_article_twentyFour(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentyFour")

    def test_article_twentyFive(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentyFive")

    def test_article_twentySix(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentySix")

    def test_article_twentySeven(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentySeven")

    def test_article_twentyEight(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentyEight")

    def test_article_twentyNine(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article TwentyNine")

    def test_article_thirty(self):
        win = u''''''
        unicode = u''''''
        result = Uni_To_Win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Test Article Thirty")

if __name__ == "__main__":
    unittest.main()
